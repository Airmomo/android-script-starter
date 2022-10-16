import time

from config import adbConfig, logConfig, yamlConfig
from util import logUtil, adbUtil
from entity.androidDevice import AndroidDevice
# ThreadPoolExecutor 多线程顺序池
# ProcessPoolExecutor 多进程顺序池
# 主要区别：线程之间可以共享某一变量，进程之间则无法共享
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def init():
    """ 初始化配置项 """
    yaml = yamlConfig.init(yamlConfig.YAML_DEV)
    adbConfig.init(yaml["adb"]["path"])
    logConfig.init(yaml["log"]["level"])
    logUtil.setLevel(yaml["syslog"]["level"])


def test():
    """ 测试程序入口 """
    """ 获取设备列表 """
    logUtil.info("当前设备列表：", adbConfig.getDevices())
    devices = adbConfig.getDevices()
    # 父线程捕获子线程抛出的异常
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(initDeviceAndRun, device_name) for device_name in devices]
        for future in futures:
            # 当子线程中异常时，这里会抛出，不处理是为了获取详细的错误内容
            result = future.result()
            if result:
                result.logger.debug("测试程序执行完毕")


def initDeviceAndRun(device_name):
    android_device = AndroidDevice(adbConfig.ADB_PATH, device_name, 720, 1280, logConfig.LOGGER_LEVEL)
    # testToucher(android_device)
    # testLongToucher(android_device)
    # testOcr(android_device)
    # testFindImage(android_device)
    # testFindColor(android_device)
    return android_device


def testFindColor(android_device):
    """ 测试找色功能 """
    match_color_str = 'DD5044-000000,-12|22|E3E3E3-000000,3|34|EFEFEF-000000'
    res = android_device.finder.findMultiColor(0, 0, 720, 1280, match_color_str)
    print(res)
    android_device.toucher.tap(res[0], res[1])


def testOcr(android_device):
    res = android_device.ocrer.checkText(833, 573, 904, 613, "注册")
    print(res)
    android_device.toucher.tap(833, 573)


def testFindImage(android_device):
    """ 测试找图功能 """
    template_path = "app/demo/static/image/auth/gotoRegister.png"
    res = android_device.finder.findImage(0, 0, 720, 1280, template_path, 0.9, match_is_show=False)
    print(res)
    android_device.toucher.tap(res[0], res[1])


def testToucher(android_device):
    """ 测试多点触控功能 """
    android_device.toucher.touchDown(250, 250, 1)
    android_device.toucher.touchMove(500, 500, 1)
    for i in range(2):
        android_device.toucher.tap(250, 500)
        time.sleep(1)
    android_device.toucher.touchUp(1)


def testLongToucher(android_device):
    """ 测试多设备同时长按 """
    android_device.toucher.longTouch(320, 250, 2000)


if __name__ == "__main__":
    """ 主程序的入口 """
    init()
    test()
