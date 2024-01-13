#!/bin/bash
word_dir=$(pwd)
file_list=$(ls)
for file in $file_list
do
    # echo "$file"
    if [[ "$file" == *.md ]]
    then
        sed -i "\[toc\]" "$file"
        echo "在文件$file添加toc成功"
        file_name="$word_dir/$file"
        doctoc "$file_name"
        sed -i "/\*\*Table of Contents\*\*  \*generated with .*\*/d" "$file_name"
        sed -i "/b\/g/d" "$file_name"
        # cat $file_name
        echo "$file删除字符串成功"
    else
        continue
    fi
done
