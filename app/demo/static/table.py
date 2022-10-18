"""
    资源数据库
"""
from plugin.tablerEx import TableColorItem, TableImageItem, TableOcrCheckItem, TableOcrReadItem, TablePositionItem, TableRangeItem


"""
    列表 = {
        表名:{
            key: value (TableItem),
        },
    }
"""
Table = {
    "模版":
        {
            "颜色": TableColorItem(0, 0, 720, 1280, "DD5044-000000,-12|22|E3E3E3-000000,3|34|EFEFEF-000000"),
            "图片": TableImageItem(0, 0, 720, 1280, "app/demo/static/image/demo.png", 0.9),
            "文本校验": TableOcrCheckItem(286, 842, 416, 881, "you love"),
            "文本识别": TableOcrReadItem(286, 842, 416, 881),
            "坐标": TablePositionItem(520, 520),
            "范围": TableRangeItem(250, 250, 520, 520),
        },
}
