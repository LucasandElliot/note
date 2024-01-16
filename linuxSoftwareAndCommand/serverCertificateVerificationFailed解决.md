[toc]

# server certificate verification failed. CAfile etcsslcertsca-certificates.crt CRLfile none报错

- 主要错误常见场景
  - apt-get update命令的时候井镜像源自身问题，http的问题等
  - 在git clone的时候遇见该错误
- 出现原因
  - 因为时间差别太大
  - 镜像源或者git错误配置

- 解决方法【针对于git而言】

  - ```
    export GIT_SSL_NO_VERIFY=1
    ```

  - ```
    git config --global http.sslverify false
    ```

  - 更换时间，随后重装

    - ```
      date -R
      apt-get install ntp
      
      ```

    - 

  - 重新安装ca-certificates

    - ```
      sudo apt-get install --reinstall ca-certificates
      sudo mkdir /usr/local/share/ca-certificates/cacert.org
      sudo wget -P /usr/local/share/ca-certificates/cacert.org http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt
      sudo update-ca-certificates
      git config --global http.sslCAinfo /etc/ssl/certs/ca-certificates.crt
      ```

  - 填充hostname和端口，随后执行

    - ```
      hostname=XXX
      port=443
      trust_cert_file_location=`curl-config --ca`
      
      sudo bash -c "echo -n | openssl s_client -showcerts -connect $hostname:$port -servername $hostname \
          2>/dev/null  | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p'  \
          >> $trust_cert_file_location"
      ```

  - 解决办法【对于apt-get/apt update而言】
    - 直接选择将https开头的源更换为http即可，随后重新执行命令

# 参考

[stack解决Server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none](https://stackoverflow.com/questions/21181231/server-certificate-verification-failed-cafile-etc-ssl-certs-ca-certificates-c)

