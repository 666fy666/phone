import xlrd
import colorama
from colorama import Fore, Back, Style  # 命令行颜色字体库
import color

colorama.init(autoreset=True)  # 使旧版cmd中命令行颜色字体生效, 并在print换行处自动还原默认颜色


def red(some_str):
    return Fore.LIGHTRED_EX + some_str + Fore.RESET


def yellow(some_str):
    return Fore.YELLOW + some_str + Fore.RESET


def blue(some_str):
    return Fore.LIGHTBLUE_EX + some_str + Fore.RESET


def green(some_str):
    return Fore.GREEN + some_str + Fore.RESET


def white(some_str):
    return Fore.WHITE + some_str + Fore.RESET


def tiku(res):
    FileContaceList = 'fy.xls'
    FileName = FileContaceList
    # open file
    FileObj = xlrd.open_workbook(FileName)
    # 获取第一个工作表
    sheet = FileObj.sheets()[0]
    # 行数
    row_count = sheet.nrows
    # 列数
    col_count = sheet.ncols

    KeyStr = res
    print(KeyStr)
    ct = 0
        # 搜索关键字符串
    for element in range(row_count):
        if KeyStr in str(sheet.row_values(element)[0]):
            print(color.yellow("题库中第%s题" % sheet.row_values(element)[2]))
            print(color.white("题目：【%s】" % sheet.row_values(element)[0]))
            print(color.red("答案：%s" % sheet.row_values(element)[1]))
            print("（请仔细核对选项，考试可能会乱序！！！）")
            ct = ct + 0
        else:
            ct = ct + 1
        if ct == row_count:
            pass
    print("搜索结束")
