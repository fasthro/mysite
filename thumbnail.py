# 针对文章内图片进行缩略图生成工具
# 只生成 img-*.* 的图片
# python thumbnail.py blog_article/static/article/mz/img/20180526
import os
import sys
import time
from PIL import Image
from multiprocessing.dummy import Pool as ThreadPool


SIZE = (1024, 1024)


def get_imgs(filename):
    fp = os.path.join(os.getcwd(), filename)
    fps = []
    if os.path.isfile(fp):
        fps.append(fp)
        return fps
    else:
        for f in os.listdir(fp):
            basename = os.path.splitext(f)[0]
            bs = basename.split('-')
            if len(bs) == 2 and bs[0] == 'img':
                fps.append(os.path.join(fp, f))
            pass
    return fps


def get_save_path(filename):
    fs = os.path.splitext(filename)
    return fs[0] + "-thumbnail" + fs[1]


def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    save_path = get_save_path(filename)
    print("> " + save_path)
    im.save(save_path)


if __name__ == '__main__':
    start = time.time()

    if len(sys.argv) > 1:
        fp = sys.argv[1]
        if os.path.exists(fp):
            images = get_imgs(fp)

            pool = ThreadPool()
            pool.map(create_thumbnail, images)
            pool.close()
            pool.join()

            end = time.time()
            t = end - start
            print("生成缩略图完毕 > 总耗时 " + str(t) + "s")


