# 使 makedown 图片转换为 baguettebox 格式
import os
import sys
import codecs


def get_baguettebox_html(line):
    line = line.strip()
    img = line[4:-1]
    ts = img.split('.')
    thumbnail = ts[0] + '-thumbnail.' + ts[1]
    return '<a class="pop-img-box" href="' + img +'"><img src="' + thumbnail + '" alt=""></a>'


def check_md_file(fp):
    ts = os.path.splitext(fp)
    tfp = ts[0] + "temp" + ts[1]
    wcode = codecs.open(tfp, 'a', 'utf-8')
    rcode = codecs.open(fp, 'r', 'utf-8')
    for line in rcode.readlines():
        if line[:4] == '![](':
            wcode.write(get_baguettebox_html(line))
            wcode.write("\n")
        else:
            wcode.write(line)

    rcode.flush()
    rcode.close()

    wcode.flush()
    wcode.close()

    os.remove(fp)
    os.rename(tfp, fp)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        fp = sys.argv[1]

        if os.path.exists(fp):
            check_md_file(fp);