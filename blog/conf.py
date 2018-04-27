# blog 配置文件

# 资源路径
STATIC_URL = '../static/'
# img 路径
STATIC_IMG_URL = STATIC_URL + 'img/'
# head 路径
STATIC_HEAD_URL = STATIC_IMG_URL + 'head/'
# article 路径
STATIC_ARCTLE_URL = STATIC_IMG_URL + 'article/'


# main view conf
MAIN_PAGE_NUM = 8

# article conf

# 默认文章 img 路径
DEFAULT_ARTICLE_IMG_URL = STATIC_ARCTLE_URL + 'default-article-img.png'


# user conf

# 默认头像路径
DEFAULT_HEAD_URL = STATIC_HEAD_URL + 'default-head.jpg'
# 默认个人介绍
DEFAULT_INTRODUCTION = "作者很懒，没有留下任何足迹..."
# Github url
DEFAULT_GITHUB_URL = 'https://github.com/fasthro'
