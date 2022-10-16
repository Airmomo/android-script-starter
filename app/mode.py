"""
    实现具体功能的模式
    当前模式为：默认启动模式
"""


class Mode:

    # 模式名称
    MODE_NAME = "模式接口"

    def __init__(self, android_device):
        """
            初始化模式，解包安卓设备对象，隐藏不必要的数据对象，模式只通过组件/插件来实现操作\n
            :param android_device: 安卓设备对象
        """
        self.device_name = android_device.device_name
        self.activity_manager = android_device.activity_manager
        self.logger = android_device.logger
        self.phone = android_device.phone
        self.screenshoter = android_device.screenshoter
        self.toucher = android_device.toucher
        self.finder = android_device.finder
        self.ocrer = android_device.ocrer
        self.switcher = android_device.switcher
        self.timer = android_device.timer
        self.tabler_ex = android_device.tabler_ex
        self.finder_ex = android_device.finder_ex
        self.ocrer_ex = android_device.ocrer_ex

    def primaryStart(self):
        """
            模式启动，实现功能的入口函数
            :return: None
        """
        pass
