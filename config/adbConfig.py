import subprocess
from util import adbUtil

# ADB文件路径
# 注意如果目录的命名不能出现关键字或标识符，如tool是py中的关键字，如果以tool作为目录名称则会导致无法定位到该文件路径
# 需要将tool改为tools作为目录名才行
ADB_PATH_MAC = "/Users/caizhuohan/PycharmProjects/GamerHelper/tools/api33/platform-tools-mac/adb"
ADB_PATH_WINDOWS = "/Users/caizhuohan/PycharmProjects/GamerHelper/tools/api33/platform-tools-windows/adb"
ADB_PATH_LINUX = "/Users/caizhuohan/PycharmProjects/GamerHelper/tools/api33/platform-tools-linux/adb"
ADB_PATH = ADB_PATH_MAC


def init(adb_path):
    global ADB_PATH
    ADB_PATH = adb_path
    """ 重新启动ADB """
    subprocess.getoutput(f"{ADB_PATH} kill-server")
    subprocess.getoutput(f"{ADB_PATH} start-server")
    """ 刷新设备列表 """
    subprocess.getoutput(f"{ADB_PATH} devices")


def getDevices():
    """ 获取设备列表 """
    return adbUtil.getDevices(ADB_PATH)
