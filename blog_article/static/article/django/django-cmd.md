###django常用命令

------------


#####&nbsp; 创建项目
`djnago-admin createproject project_name`

------------


#####&nbsp; 创建 APP
`python manage.py startapp app_name`

------------

#####&nbsp; 创建管理员
`python manage.py createsuperuser`

------------

#####&nbsp; 开启服务器
`python manage.py runserver [ip]|[port]|[ip:port]`

------------
#####&nbsp; 创建数据库迁移文件
`python manage.py makemigrations [app_name [app_name ...]]`

------------

#####&nbsp;  同步模型到数据
`python manage.py migrate`

------------
#####&nbsp;  启动数据库命令解释器
`python manage.py dbshell`


------------


#####&nbsp;  启动 python 交互解释器
`python manage.py shell` `... -i ipython` `... -i bpython`

------------
#####&nbsp; 收集 static 目录资源
`python manage.py collectstatic`

------------


<br>
>以上这些都是常用的命令，具体请查看[官方文档](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/)