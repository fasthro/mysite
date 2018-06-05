
### djano 采坑记录

#### 第一坑

    Unhandled exception in thread started by <function check_errors.<locals>.wrapper at 0x0000000003CEE8C8>
    Traceback (most recent call last):
      File "C:\ProgramData\Anaconda3\envs\blog\lib\site-packages\django\db\backends\mysql\base.py", line 15, in <module>
        import MySQLdb as Database
    ModuleNotFoundError: No module named 'MySQLdb'

**填坑方法**
在django 项目的 __init__.py 中加入如下代码

    import pymysql
    pymysql.install_as_MySQLdb()

#### 第二坑
![](http://localhost:8000/static/article/django/img/trouble/trouble-2.png)

**填坑方法**

```python
# 出错代码为
author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')

# 修改方法，在后面添加 on_delete=models.CASCADE
author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
```

#### 第三坑
![](http://localhost:8000/static/article/django/img/trouble/trouble-3.png)

**填坑方法**
需要执行 python manage.py makemigrations 创建数据迁移

#### 第四坑
![](http://localhost:8000/static/article/django/img/trouble/trouble-4.png)

**填坑方法**
删除原有数据库之后再重新建立数据库，然后在执行 python manage.py migrate

#### 第五坑
在使用 django 静态文件方法的时候出的问题
![](http://localhost:8000/static/article/django/img/trouble/trouble-5.png)

**填坑方法**
在使用 "{% static "" %}" 方式访问静态资源的时候要加上 {% load static %} 

#### 第六坑
集成了 editor.md 来转化 makedown 到 html 时候，bootstrap 中设置了 code 的全局样式，editor.md 导致转化后的样式与 editor.md 编辑器中显示不一致问题。

**填坑方法**
果断的删除了 bootstrap.css 中的 code 样式的相关设置

#### 第七坑
集成了 editor.md 来转化 makedown 到 html 时候,第一行总是转换失败，如图
![](http://localhost:8000/static/article/django/img/trouble/trouble-7-1.png)

**填坑方法**
把 makedown 第一行空出来或者加入注释
![](http://localhost:8000/static/article/django/img/trouble/trouble-7-2.png)
