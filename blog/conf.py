import os
from mysite import settings
# blog 配置文件

# img 路径
STATIC_IMG_URL = os.path.join(settings.STATIC_URL, 'img')
# head 路径
STATIC_HEAD_URL = os.path.join(settings.STATIC_URL, 'head')
# article 路径
STATIC_ARCTLE_URL = os.path.join(settings.STATIC_URL, 'article')
STATIC_ARCTLE_ROOT = os.path.join(settings.STATIC_ROOT, 'article')


# main view conf
MAIN_PAGE_NUM = 8

# article conf

# 默认文章 img 路径
DEFAULT_ARTICLE_IMG_URL = STATIC_IMG_URL + '/default-article-banner.jpg'


# 获取正文文件上传路径
def get_article_content_file_upload_path(instance, filename):
    ns = filename.split('-')

    if len(ns) <= 1:
        up = STATIC_ARCTLE_ROOT
    else:
        up = os.path.join(STATIC_ARCTLE_ROOT, ns[0])

    if os.path.exists(up) is None:
        os.makedirs(up)

    fp = os.path.join(up, filename)
    if os.path.exists(fp):
        os.remove(fp)

    return fp


# user conf

# 默认头像路径
DEFAULT_HEAD_URL = STATIC_HEAD_URL + 'default-head.jpg'
# 默认个人介绍
DEFAULT_INTRODUCTION = "作者很懒，没有留下任何足迹..."
# Github url
DEFAULT_GITHUB_URL = 'https://github.com/fasthro'
