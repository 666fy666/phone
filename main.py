import os  # 导入以后可以使用shell命令，python自带不用安装
import re
from PIL import Image  # PIL是一个对图片处理的库   python3 使用 pip install pillow 安装
from tiku import tiku
import time
from cnocr import CnOcr

for i in range(0, 9999):
    os.system('adb shell screencap -p /sdcard/ocr.png')  # 截屏并将图片保存到手机
    os.system('adb pull /sdcard/ocr.png D:/github/phone/ocr.png')  # 讲手机内保存的截屏发送到电脑指定文件夹
    print("开始截图！！！")
    # 这里的文件路径根据你自己系统的文件路径来填
    im = Image.open("ocr.png")
    size = (0, 0, 1080, 2400)  # 第一个参数87是一到九十九题，132是100题以后
    after_cut = im.crop(size)  # crop需要的参数为（左，上，右，下）
    after_cut.save("ocr.png")  # 保存修剪后的图片
    im.close()  # 使用open以后随时记得close~~~
    print("图片修剪完成")
    ocr = CnOcr()
    res = ocr.ocr('ocr.png')
    time.sleep(1)
    res = res[0][0]
    res = ''.join(res)
    res = re.findall(r'[\w]+', res)
    res = ''.join(res)
    res = res[0:4]
    tiku(str(res))
    input("按回车键继续（如没有反应就再按一次）:")
