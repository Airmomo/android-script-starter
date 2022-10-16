"""日志级别"""
LEVEL_DEBUG = 5
LEVEL_INFO = 4
LEVEL_WARNING = 3
LEVEL_ERROR = 2
LEVEL_CRITICAL = 1
"""当前日志级别"""
LOGGER_LEVEL = LEVEL_DEBUG


def init(logger_level='debug'):
    global LOGGER_LEVEL
    """ 设置日志等级 """
    if logger_level == 'debug':
        LOGGER_LEVEL = LEVEL_DEBUG
    elif logger_level == 'info':
        LOGGER_LEVEL = LEVEL_INFO
    elif logger_level == 'warning':
        LOGGER_LEVEL = LEVEL_WARNING
    elif logger_level == 'error':
        LOGGER_LEVEL = LEVEL_ERROR
    elif logger_level == 'critical':
        LOGGER_LEVEL = LEVEL_CRITICAL
    else:
        LOGGER_LEVEL = LEVEL_DEBUG


