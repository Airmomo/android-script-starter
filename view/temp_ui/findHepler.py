# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findHepler.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.image_scrollArea.setGeometry(QtCore.QRect(10, 10, 650, 600))
        self.image_scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.image_scrollArea.setWidgetResizable(True)
        self.image_scrollArea.setObjectName("image_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 650, 600))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(650, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.image_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 800, 1360))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(800, 1360))
        self.image_label.setMouseTracking(False)
        self.image_label.setText("")
        self.image_label.setPixmap(QtGui.QPixmap("../../temp/emulator-5554/screenshot.png"))
        self.image_label.setScaledContents(False)
        self.image_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.image_label.setWordWrap(False)
        self.image_label.setObjectName("image_label")
        self.image_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(670, 40, 375, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.operation_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.operation_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.operation_layout.setContentsMargins(10, 10, 10, 10)
        self.operation_layout.setObjectName("operation_layout")
        self.file_layout = QtWidgets.QHBoxLayout()
        self.file_layout.setObjectName("file_layout")
        self.load_image_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.load_image_button.setAccessibleName("")
        self.load_image_button.setObjectName("load_image_button")
        self.file_layout.addWidget(self.load_image_button)
        self.load_adb_image_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.load_adb_image_button.setObjectName("load_adb_image_button")
        self.file_layout.addWidget(self.load_adb_image_button)
        self.operation_layout.addLayout(self.file_layout)
        self.findHepler_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.findHepler_tip.setEnabled(True)
        self.findHepler_tip.setAlignment(QtCore.Qt.AlignCenter)
        self.findHepler_tip.setObjectName("findHepler_tip")
        self.operation_layout.addWidget(self.findHepler_tip)
        self.position_layout = QtWidgets.QHBoxLayout()
        self.position_layout.setContentsMargins(0, 0, 0, 0)
        self.position_layout.setObjectName("position_layout")
        self.position_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_title.setObjectName("position_title")
        self.position_layout.addWidget(self.position_title)
        self.position_x_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_x_tip.setObjectName("position_x_tip")
        self.position_layout.addWidget(self.position_x_tip)
        self.position_x = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_x.setObjectName("position_x")
        self.position_layout.addWidget(self.position_x)
        self.position_y_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_y_tip.setObjectName("position_y_tip")
        self.position_layout.addWidget(self.position_y_tip)
        self.position_y = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_y.setObjectName("position_y")
        self.position_layout.addWidget(self.position_y)
        self.position_rgb_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_rgb_tip.setObjectName("position_rgb_tip")
        self.position_layout.addWidget(self.position_rgb_tip)
        self.position_rgb = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.position_rgb.setObjectName("position_rgb")
        self.position_layout.addWidget(self.position_rgb)
        self.operation_layout.addLayout(self.position_layout)
        self.crop_layout_main = QtWidgets.QHBoxLayout()
        self.crop_layout_main.setContentsMargins(0, 0, 0, 0)
        self.crop_layout_main.setObjectName("crop_layout_main")
        self.crop_range_layout = QtWidgets.QVBoxLayout()
        self.crop_range_layout.setContentsMargins(-1, -1, 0, -1)
        self.crop_range_layout.setObjectName("crop_range_layout")
        self.crop_start_layout = QtWidgets.QHBoxLayout()
        self.crop_start_layout.setObjectName("crop_start_layout")
        self.crop_start_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_start_tip.setObjectName("crop_start_tip")
        self.crop_start_layout.addWidget(self.crop_start_tip)
        self.crop_start_x_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_start_x_tip.setObjectName("crop_start_x_tip")
        self.crop_start_layout.addWidget(self.crop_start_x_tip)
        self.crop_start_x = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_start_x.setObjectName("crop_start_x")
        self.crop_start_layout.addWidget(self.crop_start_x)
        self.crop_start_y_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_start_y_tip.setObjectName("crop_start_y_tip")
        self.crop_start_layout.addWidget(self.crop_start_y_tip)
        self.crop_start_y = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_start_y.setObjectName("crop_start_y")
        self.crop_start_layout.addWidget(self.crop_start_y)
        self.crop_range_layout.addLayout(self.crop_start_layout)
        self.crop_end_layout = QtWidgets.QHBoxLayout()
        self.crop_end_layout.setObjectName("crop_end_layout")
        self.crop_end_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_end_tip.setObjectName("crop_end_tip")
        self.crop_end_layout.addWidget(self.crop_end_tip)
        self.crop_end_x_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_end_x_tip.setObjectName("crop_end_x_tip")
        self.crop_end_layout.addWidget(self.crop_end_x_tip)
        self.crop_end_x = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_end_x.setObjectName("crop_end_x")
        self.crop_end_layout.addWidget(self.crop_end_x)
        self.crop_end_y_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_end_y_tip.setObjectName("crop_end_y_tip")
        self.crop_end_layout.addWidget(self.crop_end_y_tip)
        self.crop_end_y = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.crop_end_y.setObjectName("crop_end_y")
        self.crop_end_layout.addWidget(self.crop_end_y)
        self.crop_range_layout.addLayout(self.crop_end_layout)
        self.crop_layout_main.addLayout(self.crop_range_layout)
        self.crop_option_layout = QtWidgets.QVBoxLayout()
        self.crop_option_layout.setObjectName("crop_option_layout")
        self.crop_range_copy_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.crop_range_copy_button.setObjectName("crop_range_copy_button")
        self.crop_option_layout.addWidget(self.crop_range_copy_button)
        self.crop_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.crop_save_button.setObjectName("crop_save_button")
        self.crop_option_layout.addWidget(self.crop_save_button)
        self.crop_layout_main.addLayout(self.crop_option_layout)
        self.operation_layout.addLayout(self.crop_layout_main)
        self.multi_color_res_layout = QtWidgets.QHBoxLayout()
        self.multi_color_res_layout.setContentsMargins(0, 0, 0, 0)
        self.multi_color_res_layout.setObjectName("multi_color_res_layout")
        self.multi_color_res_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.multi_color_res_title.setObjectName("multi_color_res_title")
        self.multi_color_res_layout.addWidget(self.multi_color_res_title)
        self.multi_color_res_str = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.multi_color_res_str.setObjectName("multi_color_res_str")
        self.multi_color_res_layout.addWidget(self.multi_color_res_str)
        self.multi_color_res_copy = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.multi_color_res_copy.setObjectName("multi_color_res_copy")
        self.multi_color_res_layout.addWidget(self.multi_color_res_copy)
        self.operation_layout.addLayout(self.multi_color_res_layout)
        self.color_check_tip = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.color_check_tip.setObjectName("color_check_tip")
        self.operation_layout.addWidget(self.color_check_tip)
        self.color_check_layout_main = QtWidgets.QVBoxLayout()
        self.color_check_layout_main.setObjectName("color_check_layout_main")
        self.color_check_layout_1 = QtWidgets.QHBoxLayout()
        self.color_check_layout_1.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_1.setObjectName("color_check_layout_1")
        self.color_check_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_1.setObjectName("color_check_1")
        self.color_check_layout_1.addWidget(self.color_check_1)
        self.color_x_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_1.setEnabled(False)
        self.color_x_1.setObjectName("color_x_1")
        self.color_check_layout_1.addWidget(self.color_x_1)
        self.color_y_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_1.setEnabled(False)
        self.color_y_1.setObjectName("color_y_1")
        self.color_check_layout_1.addWidget(self.color_y_1)
        self.color_RGB_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_1.setEnabled(False)
        self.color_RGB_1.setObjectName("color_RGB_1")
        self.color_check_layout_1.addWidget(self.color_RGB_1)
        self.color_offset_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_1.setObjectName("color_offset_1")
        self.color_check_layout_1.addWidget(self.color_offset_1)
        self.color_check_layout_main.addLayout(self.color_check_layout_1)
        self.color_check_layout_2 = QtWidgets.QHBoxLayout()
        self.color_check_layout_2.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_2.setObjectName("color_check_layout_2")
        self.color_check_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_2.setObjectName("color_check_2")
        self.color_check_layout_2.addWidget(self.color_check_2)
        self.color_x_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_2.setEnabled(False)
        self.color_x_2.setObjectName("color_x_2")
        self.color_check_layout_2.addWidget(self.color_x_2)
        self.color_y_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_2.setEnabled(False)
        self.color_y_2.setObjectName("color_y_2")
        self.color_check_layout_2.addWidget(self.color_y_2)
        self.color_RGB_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_2.setEnabled(False)
        self.color_RGB_2.setObjectName("color_RGB_2")
        self.color_check_layout_2.addWidget(self.color_RGB_2)
        self.color_offset_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_2.setObjectName("color_offset_2")
        self.color_check_layout_2.addWidget(self.color_offset_2)
        self.color_check_layout_main.addLayout(self.color_check_layout_2)
        self.color_check_layout_3 = QtWidgets.QHBoxLayout()
        self.color_check_layout_3.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_3.setObjectName("color_check_layout_3")
        self.color_check_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_3.setObjectName("color_check_3")
        self.color_check_layout_3.addWidget(self.color_check_3)
        self.color_x_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_3.setEnabled(False)
        self.color_x_3.setObjectName("color_x_3")
        self.color_check_layout_3.addWidget(self.color_x_3)
        self.color_y_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_3.setEnabled(False)
        self.color_y_3.setObjectName("color_y_3")
        self.color_check_layout_3.addWidget(self.color_y_3)
        self.color_RGB_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_3.setEnabled(False)
        self.color_RGB_3.setObjectName("color_RGB_3")
        self.color_check_layout_3.addWidget(self.color_RGB_3)
        self.color_offset_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_3.setObjectName("color_offset_3")
        self.color_check_layout_3.addWidget(self.color_offset_3)
        self.color_check_layout_main.addLayout(self.color_check_layout_3)
        self.color_check_layout_4 = QtWidgets.QHBoxLayout()
        self.color_check_layout_4.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_4.setObjectName("color_check_layout_4")
        self.color_check_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_4.setObjectName("color_check_4")
        self.color_check_layout_4.addWidget(self.color_check_4)
        self.color_x_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_4.setEnabled(False)
        self.color_x_4.setObjectName("color_x_4")
        self.color_check_layout_4.addWidget(self.color_x_4)
        self.color_y_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_4.setEnabled(False)
        self.color_y_4.setObjectName("color_y_4")
        self.color_check_layout_4.addWidget(self.color_y_4)
        self.color_RGB_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_4.setEnabled(False)
        self.color_RGB_4.setObjectName("color_RGB_4")
        self.color_check_layout_4.addWidget(self.color_RGB_4)
        self.color_offset_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_4.setObjectName("color_offset_4")
        self.color_check_layout_4.addWidget(self.color_offset_4)
        self.color_check_layout_main.addLayout(self.color_check_layout_4)
        self.color_check_layout_5 = QtWidgets.QHBoxLayout()
        self.color_check_layout_5.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_5.setObjectName("color_check_layout_5")
        self.color_check_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_5.setObjectName("color_check_5")
        self.color_check_layout_5.addWidget(self.color_check_5)
        self.color_x_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_5.setEnabled(False)
        self.color_x_5.setObjectName("color_x_5")
        self.color_check_layout_5.addWidget(self.color_x_5)
        self.color_y_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_5.setEnabled(False)
        self.color_y_5.setObjectName("color_y_5")
        self.color_check_layout_5.addWidget(self.color_y_5)
        self.color_RGB_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_5.setEnabled(False)
        self.color_RGB_5.setObjectName("color_RGB_5")
        self.color_check_layout_5.addWidget(self.color_RGB_5)
        self.color_offset_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_5.setObjectName("color_offset_5")
        self.color_check_layout_5.addWidget(self.color_offset_5)
        self.color_check_layout_main.addLayout(self.color_check_layout_5)
        self.color_check_layout_6 = QtWidgets.QHBoxLayout()
        self.color_check_layout_6.setContentsMargins(0, 0, 0, 0)
        self.color_check_layout_6.setObjectName("color_check_layout_6")
        self.color_check_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.color_check_6.setObjectName("color_check_6")
        self.color_check_layout_6.addWidget(self.color_check_6)
        self.color_x_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_x_6.setEnabled(False)
        self.color_x_6.setObjectName("color_x_6")
        self.color_check_layout_6.addWidget(self.color_x_6)
        self.color_y_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_y_6.setEnabled(False)
        self.color_y_6.setObjectName("color_y_6")
        self.color_check_layout_6.addWidget(self.color_y_6)
        self.color_RGB_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_RGB_6.setEnabled(False)
        self.color_RGB_6.setObjectName("color_RGB_6")
        self.color_check_layout_6.addWidget(self.color_RGB_6)
        self.color_offset_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.color_offset_6.setObjectName("color_offset_6")
        self.color_check_layout_6.addWidget(self.color_offset_6)
        self.color_check_layout_main.addLayout(self.color_check_layout_6)
        self.operation_layout.addLayout(self.color_check_layout_main)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FindHelper"))
        self.load_image_button.setText(_translate("MainWindow", "打开本地图片"))
        self.load_adb_image_button.setText(_translate("MainWindow", "获取模拟器截图"))
        self.findHepler_tip.setText(_translate("MainWindow", "点击图片的任意位置，即可获取对应位置的坐标信息"))
        self.position_title.setText(_translate("MainWindow", "当前坐标"))
        self.position_x_tip.setText(_translate("MainWindow", "x："))
        self.position_x.setText(_translate("MainWindow", "0"))
        self.position_y_tip.setText(_translate("MainWindow", "y："))
        self.position_y.setText(_translate("MainWindow", "0"))
        self.position_rgb_tip.setText(_translate("MainWindow", "RGB："))
        self.position_rgb.setText(_translate("MainWindow", "RGB"))
        self.crop_start_tip.setText(_translate("MainWindow", "裁剪起点"))
        self.crop_start_x_tip.setText(_translate("MainWindow", "x："))
        self.crop_start_x.setText(_translate("MainWindow", "0"))
        self.crop_start_y_tip.setText(_translate("MainWindow", "y："))
        self.crop_start_y.setText(_translate("MainWindow", "0"))
        self.crop_end_tip.setText(_translate("MainWindow", "裁剪终点"))
        self.crop_end_x_tip.setText(_translate("MainWindow", "x："))
        self.crop_end_x.setText(_translate("MainWindow", "0"))
        self.crop_end_y_tip.setText(_translate("MainWindow", "y："))
        self.crop_end_y.setText(_translate("MainWindow", "0"))
        self.crop_range_copy_button.setText(_translate("MainWindow", "复制区域坐标"))
        self.crop_save_button.setText(_translate("MainWindow", "保存裁剪区域"))
        self.multi_color_res_title.setText(_translate("MainWindow", "多点找色"))
        self.multi_color_res_copy.setText(_translate("MainWindow", "复制"))
        self.color_check_tip.setText(_translate("MainWindow", "利用快捷键：Ctrl / Comand + 数字1～6 可记录当前坐标信息"))
        self.color_check_1.setText(_translate("MainWindow", "选中"))
        self.color_offset_1.setText(_translate("MainWindow", "000000"))
        self.color_check_2.setText(_translate("MainWindow", "选中"))
        self.color_offset_2.setText(_translate("MainWindow", "000000"))
        self.color_check_3.setText(_translate("MainWindow", "选中"))
        self.color_offset_3.setText(_translate("MainWindow", "000000"))
        self.color_check_4.setText(_translate("MainWindow", "选中"))
        self.color_offset_4.setText(_translate("MainWindow", "000000"))
        self.color_check_5.setText(_translate("MainWindow", "选中"))
        self.color_offset_5.setText(_translate("MainWindow", "000000"))
        self.color_check_6.setText(_translate("MainWindow", "选中"))
        self.color_offset_6.setText(_translate("MainWindow", "000000"))