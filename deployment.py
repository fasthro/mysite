# 部署服务器

import os
import shutil
from git import Repo
from django.core import management
import codecs
import platform

cwd = os.getcwd()

# 开发服务器
dev_server = 'localhost:8000'
# 正式服务器
live_server = '39.106.221.18'

print('********** 服务器部署开始 ********')
print('git pull')
# git pull
repo = Repo(cwd)
remote = repo.remote()
remote.pull()


print('manage.py collectstatic')
# 清空 static 目录
static_url = os.path.join(cwd, 'static')
if os.path.exists(static_url):
    try:
        shutil.rmtree(static_url)

        if not os.path.exists(static_url):
            os.mkdir(static_url)
    finally:
        pass


# 执行收集静态文件命令
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
management.execute_from_command_line(['manage.py', 'collectstatic'])


print('replace md-file server')
# 修改 makedown 文件内的图片链接地址为当前服务器
article_root = os.path.join(cwd, 'static/article/')


# 获取所有的 md-file 路径
def get_md_file_paths(rp, mdps):
    if os.path.exists(rp):
        for item in os.listdir(rp):
            tp = os.path.join(rp, item)
            if os.path.isfile(tp):
                fix = os.path.splitext(tp)
                if len(fix) == 2 and fix[1] == '.md':
                    mdps.append(tp)
            else:
                get_md_file_paths(tp, mdps)


# 替换 md-file 里的图片地址为当前服务器
def replace_md_img_url(mdp):
    wmdp = mdp + ".temp"
    if os.path.exists(wmdp):
        os.remove(wmdp)

    wcode = codecs.open(wmdp, 'a', 'utf-8')
    rcode = codecs.open(mdp, 'r', 'utf-8')
    for line in rcode.readlines():
        text = line.replace(dev_server, live_server)
        wcode.write(text)

    rcode.flush()
    rcode.close()

    wcode.flush()
    wcode.close()

    os.remove(mdp)
    os.rename(wmdp, mdp)


if os.path.exists(article_root):
    mdps = []

    get_md_file_paths(article_root, mdps)

    for md in mdps:
        replace_md_img_url(md)

if platform.system() == "Linux":
    # 重启 uwsgi 服务
    pid_url = os.path.join(cwd, 'uwsgi.pid')
    if os.path.exists(pid_url):
        print('kill uwsgi')
        pcode = codecs.open(pid_url, 'r', 'utf-8')
        pid = pcode.readline().strip('\n')
        pcode.close()

        os.system('kill -9 ' + pid)

    print('restart uwsgi')
    os.system('uwsgi --ini uwsgi.ini')


    # 重启 nginx
    print('restart nginx')
    os.system('/etc/init.d/nginx restart')

print("platform : " + platform.system())
print('********** 服务器部署完毕 ********')