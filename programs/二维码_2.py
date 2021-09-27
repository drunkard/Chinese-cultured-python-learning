#!/cc/bin/python3
import qrcode
import sys

try:
    print('输入要转换成二维码的文字或 URL，按 Ctrl-C 退出')
    while True:
        i = input('请输入 URL 或文字: ')
        qrcode.run_example(i)
except KeyboardInterrupt:
    sys.exit(0)
