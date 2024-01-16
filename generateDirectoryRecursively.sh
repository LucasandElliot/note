time_day=$(date +"%Y-%m-%d")
store_file_name="$time_day""Default.log"
touch "$store_file_name"
for file in $(find | grep md)
do
    line=$(grep -c -w "\[toc\]" "$file")
    if [[ $file == *README.md ]]
    then
        echo "跳过了介绍文件README.md"
        continue
    # 因为github支持toc直接生成，所以在这里删除所有关于toc，但是toc标签可以放置于typora等软件生成目录
    # elif [ $line -eq 0 ]
    # then
    #         sed -i "1i\[toc\]" "$file"
    # fi
    # 这里成功进入到没有被处理过的md文件
    else
    time_=$(date +'%Y-%m-%d %H:%M:%S')
    echo "$time_ 修改$file文件，加入目录" >> "$store_file_name"
    doctoc "$file" >> "$store_file_name"
    sed -i "/\*\*Table of Contents\*\*  \*generated with .*\*/d" "$file"
    sed -i "/b\/g/d" "$file"
    fi
done
echo "生成目录成功，具体请查看日志文件$store_file_name"
echo "generate directory of md files successfully, here are some details in $store_file_name"
read -p $'是否选择删除日志文件,请输入yes 或者 no\n' deleteChoice
if [ "$deleteChoice" == "yes" ]
then
    rm "$store_file_name"
    echo "删除$store_file_name成功"
fi