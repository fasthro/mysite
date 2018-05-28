
### django 部署到 Linux 服务器

写这篇文章主要是想分享一下我在部署 django 服务器的时候遇到的问题和解决办法，为同我一样没有太多服务器基础而且正在学习 django 的小伙伴节约一些脑细胞和时间。看了网上好多关于django 部署的教程，有的写的非常好，有的则是潦草几句，我在这里记录下我部署时候的每一个步骤。希望能够帮到遇到问题的你们。话不多说开整...

Linux 服务器是阿里云的，系统为 Ubuntu 16.04 64位

#### 安装 python3 环境
我用的是 anaconda, 我个人觉得这个对包管理和环境管理也很方便

**下载 anaconda3.5 **

`wget https://repo.anaconda.com/archive/Anaconda3-5.1.0-Linux-x86_64.sh`

**安装 anaconda3 **

`bash Anaconda3-5.1.0-Linux-x86_64.sh`

![](http://localhost:8000/static/article/django/img/deployment_server-1.png)

回车很多次继续

![](http://localhost:8000/static/article/django/img/deployment_server-2.png)

输入 yes 回车继续

![](http://localhost:8000/static/article/django/img/deployment_server-3.png)

回车开始进行安装，在此只需要耐心等待

![](http://localhost:8000/static/article/django/img/deployment_server-4.png)

是否添加到环境变量的询问，输入 yes 回车

![](http://localhost:8000/static/article/django/img/deployment_server-5.png)

安装 vscode 的询问，我这里就不安装了,输入 no 回车，安装完成。

**测试 anaconda3 是否可以正常工作**

执行 `conda -V`命令查看 conda 版本号

![](http://localhost:8000/static/article/django/img/deployment_server-6.png)

发现没有 conda 这个命令，原因是没有把anaconda3 加入到系统环境变量中导致的问题。

**永久添加 anaconda3 到系统环境变量**

执行 `vi etc/profile` 打开 `profile` 文件，把 `export PATH=/root/anaconda3/bin:$PATH` 加入到文件内容最后面。

修改后如图:

![](http://localhost:8000/static/article/django/img/deployment_server-7.png)

修改完后保存退出 vi,执行 `source /etc/profile` 使修改马上生效，在执行 `conda -V` 命令就显示了 conda 当前版本

**创建 python 环境**

执行 `conda create --name blog python=3.6` 命令创建 *python 3.6* 版本名为 *blog* 的环境，

或者

执行 `conda create --name blog python=3.6 django pymysql` 创建环境的同时还会在此环境中安装 *django* 和 *pymysql* 包

执行 `conda env list` 命令查看所有环境

![](http://localhost:8000/static/article/django/img/deployment_server-8.png)

执行 ` conda install -n blog django` 来为 *blog* 环境安装 *django*

执行 `conda list -n blog` 查看 *blog* 环境中包列表，来验证我们是否把自己已经安装的包安装成功

执行 `source activate blog` 进入blog 环境

执行 `source deactivate blog` 退出blog 环境

####nginx

**安装 nginx**

执行 `apt-get update`

执行 `apt-get install nginx`

**检查 nginx 安装是否成功**

执行 `nginx -v`

![](http://localhost:8000/static/article/django/img/deployment_server-9.png)

**nginx 命令**

启动 `/etc/init.d/nginx start`

关闭 `/etc/init.d/nginx stop`

重启 `/etc/init.d/nginx restart`

**检查 nginx 是否启动成功**

执行 `ps -ef|grep -i nginx`

![](http://localhost:8000/static/article/django/img/deployment_server-10.png)

**卸载 nginx**

执行 `sudo apt-get --purge remove nginx`

执行 `sudo apt autoremove`

>当然在配置环境的时候是不需要卸载掉 nginx

**访问 nginx 服务器**

在浏览器里输入nginx 服务器地址端口默认为 80, 如果是云服务器，请输入云服务器外网地址。

额...无法访问到。。。。

![](http://localhost:8000/static/article/django/img/deployment_server-11.png)

由于阿里云里面有个安全组的规则设置，这个会影响到端口是否外部可以访问到，修改一下阿里云的安全组，添加一条对 80 端口的规则设置

**进入到安全组**

![](http://localhost:8000/static/article/django/img/deployment_server-12.png)

![](http://localhost:8000/static/article/django/img/deployment_server-13.png)

**添加安全组规则**

![](http://localhost:8000/static/article/django/img/deployment_server-14.png)

设置完毕，再次在浏览器访问 nginx 服务器，页面中显示如下内容，表示已经成功访问到了nginx 服务器。

![](http://localhost:8000/static/article/django/img/deployment_server-15.png)

至此 nginx 服务器安装并且成功访问到了。

####uwsgi

**安装 uwsgi**

执行 `source activate blog` 进入到我们创建的 python 环境 **blog** 中

执行 `pip install --upgrade pip` 升级 pip

执行 `pip install uwsgi` 安装 uwsgi

果然没有顺利的安装成功，遇到了如下报错

![](http://localhost:8000/static/article/django/img/deployment_server-16.png)

由于编译的时候gcc 版本导致的问题

**解决方法**
执行 `ls /usr/bin/gcc* -l` 或者 `ls usr/bin//gcc*` 查看一下本机的gcc 版本，我的服务器默认安装的是 gcc-5 的版本，这个版本太高了，所以要装 4.7 低版本的

执行 `sudo apt-get  install gcc-4.7` 安装 gcc-4.7

执行 `sudo rm /usr/bin/gcc` 删除原来系统默认的gcc

执行 `sudo ln -s /usr/bin/gcc-4.7 /usr/bin/gcc` 重新执行 4.7 版本的 gcc

再次执行 `pip install uwsgi` 安装 uwsgi，结果成功安装了

![](http://localhost:8000/static/article/django/img/deployment_server-17.png)

####mysql

**安装 mysql**

执行 `sudo apt-get update`

执行 `sudo apt-get install mysql-server` 安装 mysql 服务

![](http://localhost:8000/static/article/django/img/deployment_server-18.png)

输入**Y** 继续

![](http://localhost:8000/static/article/django/img/deployment_server-19.png)

输入登录 mysql root 用户的密码，测试期间我的数据库密码为了方便记录，输入的为 "root"

![](http://localhost:8000/static/article/django/img/deployment_server-20.png)

再次输入密码就完成了 mysql 服务的安装

下面在安装 mysql-client

执行 `sudo apt install mysql-client`

执行 `sudo apt install libmysqlclient-dev`

![](http://localhost:8000/static/article/django/img/deployment_server-21.png)

输入**Y**

安装完成我们来验证一下是否安装成功

执行 `sudo netstat -tap | grep mysql`

![](http://localhost:8000/static/article/django/img/deployment_server-22.png)

mysql 安装完成

**设置 mysql 在 ubuntu 下开放远程连接**

执行 `mysql -u root -p` , 输入密码 `root` 回车进入到 mysql

执行 sql 语句 `CREATE USER 'fasthro'@'%' IDENTIFIED BY 'fasthro';`

创建一个用户名为 fasthro ，密码为 fasthro 的新用户作为远程连接数据库的账号

执行 `GRANT ALL PRIVILEGES ON  *.*  TO fasthro@"%" IDENTIFIED BY 'fasthro' WITH GRANT OPTION;`

设置 fasthro 用户权限，允许所有权限

执行 `FLUSH PRIVILEGES;`

刷新权限信息，使上面的设置立即生效

执行 `netstat -nat | grep :3306` 发现依然是只有本地可以访问 3306 端口

![](http://localhost:8000/static/article/django/img/deployment_server-23.png)

执行 `vim /etc/mysql/mysql.conf.d/mysqld.cnf` 打开 mysql 配置文件

注释掉 `bind-address = 127.0.0.1` 这行，保存退出，修改后内容如下

![](http://localhost:8000/static/article/django/img/deployment_server-24.png)

执行 `/etc/inint.d/mysqld start` 重启 mysql

再次执行 `netstat -nat | grep :3306` 查看端口情况

![](http://localhost:8000/static/article/django/img/deployment_server-25.png)

发现不只是本地访问了，不要认为到这里就已经可以远程访问了，还需要在设置一下阿里云的安全组规则，使 3306 端口开放出来可访问

![](http://localhost:8000/static/article/django/img/deployment_server-26.png)

设置完毕之后，用闯将的新用户 fasthro 就可以远程连接到 mysql 了。

以上该安装的软件包已经安装完毕，下面我们开始部署配置项目！

####开始部署

**项目目录结构**

![](http://localhost:8000/static/article/django/img/deployment_server-27.png)

    uwsgi.ini //文件为项目 uwsgi 的配置
    nginx.conf //文件为项目 nginx 的配置

在服务器上我把项目放在 root 目录下面

    /root/mysite/

**uwsgi.ini 配置**
    # uwsgi.ini file
    [uwsgi]
    chdir=/root/mysite/
    # 项目 wsgi 文件路径
    wsgi-file=mysite/wsgi.py
    # 进程个数
    workers=5
    # 指定IP端口
    socket=127.0.0.1:8080
    # 指定静态文件
    static-map=/static=%(chdir)static
    # 启动uwsgi的用户名和用户组
    uid=root
    gid=root
    # 启用主进程
    master=true
    # 自动移除unix Socket和pid文件当服务停止的时候
    vacuum=true
    # 序列化接受的内容，如果可能的话
    thunder-lock=true
    # 启用线程
    enable-threads=true
    # 设置自中断时间
    harakiri=30
    # 设置缓冲
    post-buffering=4096
    # 日志文件
    daemonize=%(chdir)/uwsgi.log
    # pid 文件
    pidfile=%(chdir)/uwsgi.pid
    # stats
    stats=%(chdir)/uwsgi.stats


**nginx.conf 配置**
    # nginx 配置
    server {
      # 监听端口
      listen 80;
      # 服务器的名字(我这里填写的是服务器外网ip，因为我还没有域名呢)
      server_name 36.37.38.39;
      # nginx 日志
      access_log /root/mysite/nginx_access_log.log;
      # nginx 错误日志
      error_log /root/mysite/nginx_error_log.log;
      # nginx 编码
      charset  utf-8;
      # 启动压缩
      gzip on;
      # 支持压缩的类型
      gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json text/json image/jpeg image/gif image/png application/octet-stream;

      # 自定义错误页面
      # error_page 404 /404.html;
      # error_page 500 502 503 504 /50x.html;

      # 指定静态文件路径
       location /static {
         # 自动索引
         autoindex on;
         alias  /root/mysite/static/;
       }

      location / {
        # 项目根目录
        root /root/mysite;
        # nginx 反射地址,要与 uwsgi.ini 中填写一致
        uwsgi_pass 127.0.0.1:8080;
        # 导入 nginx 模块与 uwsgi 通讯
        include uwsgi_params;
      }
    }

>上面内容为配置相关,下面开始执行启动

**项目设置**

1.执行 `python  manage.py collectstatic` 收集静态文件到 mysite/static/

2.修该 settings.py 里面 DEBUG 为 False

    DEBUG = False

3.修该 settings.py 里面 ALLOWED_HOSTS

    ALLOWED_HOSTS = ['*']

如果不设置 ALLOWED_HOSTS 在启动成功后访问的时候在浏览器中会显示如下错误

    Exception Value:Invalid HTTP_HOST header: '36.37.38.39'. You may need to add '36.37.38.39' to ALLOWED_HOSTS.

**创建数据库**
这里大家要注意的是，如果执行 sql 语句 `CREATE DATABASE blog;` 创建数据，在启动django项目的时候会报如下错误

![](http://localhost:8000/static/article/django/img/deployment_server-28.png)

这是由于编码的问题导致

我们要执行

`CREATE DATABASE blog DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;`

来创建数据，就能解决掉上面编码的问题

**启动 uwsgi**

执行 `uwsgi --ini uwsgi.ini` 启动 uwsgi

fuck！！！又报错，步步有坑！！！

![](http://localhost:8000/static/article/django/img/deployment_server-29.png)

解决办法

执行 `find / -name libpcre.so.1` 查找 libpcre.so.1 所在的路径

![](http://localhost:8000/static/article/django/img/deployment_server-30.png)

那么就把 `export LD_LIBRARY_PATH=/root/anaconda3/lib:$LD_LIBRARY_PATH` 添加到系统

环境变量中。(加入到 etc/profile 文件的末尾)

再次启动终于没有报错了。

启动成功之后查看 uwsgi 日志，可以知道启动是否成功或者报错


**配置启动 nginx**

删除 nginx 的两个目录

执行 `rm -rf ../etc/nginx/sites-available/`

执行 `rm -rf ../etc/nginx/sites-enabled/`

复制项目中 nginx.conf 配置

执行 `cp mysite/nginx.conf ../etc/nginx/conf.d/`

这样 nginx 配置就完成了

>我们可以通过执行 `nginx -t` 来检查 nginx 配置文件格式是否正确

在执行 `vi ../etc/nginx/nginx.conf` 打开 nginx 默认的配置，修改用户为** root**

![](http://localhost:8000/static/article/django/img/deployment_server-31.png)

保存并退出。

执行 `/etc/init.d/nginx restart` 重启 nginx 服务, 在浏览器中访问试试吧！！！



------------

>1.静态文件访问不到可能是 /etc/nginx/nginx.conf 里 user 不是 root 的问题
>2.不管如何修该nginx的配置，但是在浏览器中总是访问到nginx欢迎页面，需要删除 /etc/nginx/sites-available/ 和 /etc/nginx/sites-enabled/ 目录

------------

**部署从头到尾，花了好几天，也怀疑过人生，也感叹过上苍，但最终还是在这条黑路上看到了光明，最终我认为笨不是我的错，如果放弃前行才是错。**