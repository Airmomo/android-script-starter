# android-script-starter
整合android-auto-helper和android-pixer-helper的安卓脚本应用快速开发手脚架
# 项目介绍
- [android-auto-helper](https://github.com/Airmomo/android-auto-helper)
- [android-pixer-helper](https://github.com/Airmomo/android-pixer-helper)
- [视频介绍及应用演示]()
# 开发环境
- 操作系统：mac系统（M1 Pro）
- Python：python 3.9
- 安卓设备：安卓模拟器（Android Studio Virtual Device）
- 安卓系统：Android 7.0 (api24、arm64)
# 项目依赖
可以通过命令`pip install -r requirements.txt`来安装以下依赖
- easyocr==1.6.2
- imutils==0.5.4
- numpy==1.23.3
- opencv_python_headless==4.5.4.60
- Pillow==9.2.0
- PyQt5==5.15.7
- PyYAML==6.0

**注意：PyQt5在Mac平台安装复杂、以及对Python3.7以上都不太兼容，直接通过pip安装可能会报错，需要自行搜索正确的安装方法，这里就不冗述了**
# 跨平台实现
**本项目与安卓设备的交互主要通过adb实现，只需要在初始化安卓对象时选择对应系统的adb文件即可**
adb文件存在目录`tools/platform-tools-*`下，也可以自行到官网下载->[传送门](https://developer.android.com/studio/command-line/adb)
- platform-tools-linux
- platform-tools-mac
- platform-tools-windows

**如果使用的是第三方的安卓模拟器，建议复制其模拟器源文件目录下的adb文件来调用**