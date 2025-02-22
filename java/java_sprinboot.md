# 琐碎

- 创建vue项目`create vue vue_env_name`

- 运行vue项目 `npm run serve`

- 安装Element ui `npm i element-ui -S`

- 切换管理员身份`runas /user:administrator cmd`

- 组件不想使用，但是需要有忽略，找到package.json中的eslintConfig，使用如下代码

  ```
  "eslintConfig": {
    "rules": {
      "vue/no-unused-components": "off"
    }
  }
  ```

- 