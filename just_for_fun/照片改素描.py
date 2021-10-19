#!/cc/bin/python3
import cv2
import path
import sys

files = []
if len(sys.argv) > 1:
    files = sys.argv[1:]
else:
    print('把照片转成素描风格，用法：\n\t{} <要转的照片>'.format(sys.argv[0]))
    sys.exit(2)

for f in files:
    fp = path.Path(f)
    if not fp.exists():
        print(f'文件不存在: {fp}')
        continue
    name, sfx = fp.name.splitext()
    newfp = fp.dirname().joinpath(name + '_素描' + '.' + sfx)

    # 读取图片
    img = cv2.imread(fp)
    # 转化成灰度图
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    # 对图片进行模糊化处理
    blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
    invblur_img = cv2.bitwise_not(blur_img)
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
    # 保存好素描风格的图片
    cv2.imwrite(newfp, sketch_img)

    # or:
    # img = cv2.imread(fp)
    # grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur_img = cv2.GaussianBlur(grey_img, (111, 111), 0)
    # sketch_img = cv2.divide(grey_img, blur_img, scale=256.0)
    # cv2.imwrite(newfp, sketch_img)
