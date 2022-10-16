from app.mode import Mode


class ModeImpl(Mode):
    # 模式名称
    MODE_NAME = "默认模式"

    def __init__(self, android_device):
        super().__init__(android_device)

    def primaryStart(self):
        self.logger.info("已启动_模式：", self.MODE_NAME)
        self.logger.debug(self.ocrer_ex.ocr("模版", "文本校验"))
        self.logger.debug(self.ocrer_ex.ocr("模版", "文本识别"))
        self.logger.debug(self.finder_ex.findTap("模版", "颜色"))
        self.logger.debug(self.finder_ex.findTap("模版", "图片"))
        self.logger.debug(self.finder_ex.tap("模版", "坐标"))
