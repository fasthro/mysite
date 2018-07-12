
## 生成 facebook 后台配置的hash key

###准备工作

** 安装 ActivePerl **

下载地址 http://www.activestate.com/activepython/downloads

配置per的bin路径到系统PATH（安装时有自动配置，选中自动配置）。

------------


** 下载 openssl **

下载地址 https://code.google.com/archive/p/openssl-for-windows/downloads

把下载下来的openssl解压到C盘根目录，C:\openssl-0.9.8d_X64，然后配置openssl的bin路径到系统PATH，下载的时候注意下载对应的版本，网上有人说不能用最新的openssl 来生成 hash key，算法上会有问题导致最终hash key 不正确。

------------

###官方文档提供的生成方法

**生成开发 hash key**
1. 首先打开命令行，进入到 jdk的bin 目录

2. 把 C:\Users\Administrator\.android\debug.keystore 拷贝到 jdk 的bin目录下（此举动为了方便命令行输入）

3. 在命令行输入

 `keytool -exportcert -alias androiddebugkey -keystore debug.keystore | openssl sha1 -binary | openssl base64`

 回车之后提示输入密钥，开发签名默认密钥为 **android**，注意 a 为小写。

**生成自己的签名文件 hash key**

1. 首先打开命令行，进入到 jdk的bin 目录

2. 把自己的签名文件 app.keystore 拷贝到 jdk 的bin目录下（此举动为了方便命令行输入）

3. 在命令行输入

 `keytool -exportcert -alias （签名的alias名字） -keystore （keystore的名字） | openssl sha1 -binary | openssl base64`

 回车之后提示输入app.keystore的密钥

**最后把这两个hash key 填入到facebook 后台就可以了**

###野生的hash key 生成方法

1. 首先打开命令行，进入到 jdk的bin 目录

2. 拷贝debug.keystore 和 自己的keystore到 jdk 的bin目录下

3. 在命令行输入

 `keytool -exportcert -alias （签名的alias名字） -keystore （keystore的名字） > key.txt`

 回车之后提示输入密钥

4. 继续输入 `openssl sha1 -binary debug.txt >key_sha.txt`

5. 继续输入 `openssl base64 -in debug_sha.txt >key_base64.txt`

6. 已经把hash key 生成在 key_base64.txt 文件里，开发环境的hash key 和 自己签名文件的hash 都可以用上面的步骤来生成










