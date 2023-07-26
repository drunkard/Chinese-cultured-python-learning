#!/cc/bin/python3
import qrcode

while True:
    i = input('请输入 URL 或文字: ')
    qrcode.run_example(i)
