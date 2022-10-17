from config import adbConfig, logConfig, yamlConfig
from util import logUtil
from entity.androidDevice import AndroidDevice
from app.starter import AppStarter
# ThreadPoolExecutor 多线程顺序池
# ProcessPoolExecutor 多进程顺序池
# 主要区别：线程之间可以共享某一变量，进程之间则无法共享
from concurrent.futures import as_completed, ThreadPoolExecutor, ProcessPoolExecutor


def init():
    """ 初始化配置项 """
    yaml = yamlConfig.init(yamlConfig.YAML_DEV)
    adbConfig.init(yaml["adb"]["path"])
    logConfig.init(yaml["log"]["level"])
    logUtil.setLevel(yaml["syslog"]["level"])


def main():
    """ 启动程序入口 """
    """ 获取设备列表 """
    logUtil.info("当前设备列表：", adbConfig.getDevices())
    devices = adbConfig.getDevices()
    task_futures = []
    # 父线程捕获子线程抛出的异常
    with ThreadPoolExecutor() as executor:
        for device_name in devices:
            task_futures.append(executor.submit(initDeviceAndRun, device_name, AppStarter.MODULE_DEFAULT))
        for future in task_futures:
            try:
                # 当子线程中异常时，这里会重新抛出
                result = future.result()
            except Exception as e:  # 捕获子线程中的异常
                # 成功捕获异常
                logUtil.error("该线程已停止 >>> main线程捕获到子线程的异常: ", e.args)
                future.result()
            else:
                result.android_device.logger.info("应用程序执行完毕")


def initDeviceAndRun(device_name, module):
    """
        线程函数：初始化安卓应用对象并启动指定的模式
        :param device_name: 待连接的安卓模拟器设备名称
        :param module: 启动的应用及模式
        :return: None
    """
    android_device = AndroidDevice(adbConfig.ADB_PATH, device_name, 720, 1280, logConfig.LOGGER_LEVEL)
    app_thread = AppStarter(android_device, module)
    app_thread.run()
    return app_thread


if __name__ == "__main__":
    """ 主程序的入口 """
    init()
    main()
