"""
    应用启动类
"""
import importlib
# 导入所需的插件
from plugin.finderEx import FinderEx
from plugin.ocrerEx import OcrerEx
from plugin.tablerEx import TablerEx


class AppStarter:
    # 应用启动模式标识，用于导入当前应用支持的功能模式
    # 模版
    MODULE_DEFAULT = "app.demo.mode.default"

    # 资源表，封装了图色识别所需的参数值和文件路径
    # 模版
    TABLE_DEFAULT = "app.demo.static.table"

    def __init__(self, android_device, mode_module):
        """
            初始化应用对象\n
            :param android_device: 安卓设备对象
            :param mode_module: 模式所在的包路径
        """
        self.android_device = android_device
        self.mode_module = mode_module
        # 根据启动模式加载对应的资源表
        table_import = importlib.import_module(self.TABLE_DEFAULT)
        # 初始化所需要的插件，在需要的模式可以自由拔插使用
        self.android_device.tabler_ex = TablerEx(table_import.Table)
        self.android_device.finder_ex = FinderEx(self.android_device.finder,  self.android_device.toucher, self.android_device.phone, self.android_device.logger, self.android_device.timer, self.android_device.tabler_ex)
        self.android_device.ocrer_ex = OcrerEx(self.android_device.ocrer, self.android_device.toucher, self.android_device.logger, self.android_device.timer, self.android_device.tabler_ex)

    def run(self):
        """
            应用启动函数
            :return:
        """
        # 注册功能模式对象并启动
        module = importlib.import_module(self.mode_module)
        mode = module.ModeImpl(self.android_device)
        mode.primaryStart()
