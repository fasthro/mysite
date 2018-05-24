
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

**安装 nginx**
