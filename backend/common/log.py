# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/10 13:49
import logging
import os
import sys
from loguru import logger
from config import config
from common.common import get_str_uuid, create_dir
from common.local import g


def logger_file() -> str:
    """ 创建日志文件名 """
    log_path = create_dir(config.LOGGER_DIR)

    """ 保留日志文件夹下最大个数(本地调试用) 
    本地调式需要多次重启, 日志轮转片不会生效 """
    file_list = os.listdir(log_path)
    if len(file_list) > 3:
        os.remove(os.path.join(log_path, file_list[0]))

    # 日志输出路径
    return os.path.join(log_path, config.LOGGER_NAME)


def correlation_id_filter(record):
    if not g.trace_id:
        g.trace_id = get_str_uuid()
    record['trace_id'] = g.trace_id
    return record


# 详见: https://loguru.readthedocs.io/en/stable/overview.html#features
fmt = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>| {thread} | <level>{level: <8}</level> | <yellow> {trace_id} </yellow> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
logger.remove()
logger_file()
logger.add(
    sys.stdout,
    # encoding=config.GLOBAL_ENCODING,
    level=config.LOGGER_LEVEL,
    colorize=True,
    # rotation=config.LOGGER_ROTATION,
    # retention=config.LOGGER_RETENTION,
    filter=correlation_id_filter,
    format=fmt,
    # enqueue=True
)


class InterceptHandler(logging.Handler):
    # 将标准logging模块生成的日志消息重定向到loguru日志库进行处理
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            # 获取与 logging 模块的日志级别（如 DEBUG、INFO 等）对应的 loguru 日志级别
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(level, record.getMessage())


def init_logger():
    # 获取所有日志记录器logger
    logger_name_list = [name for name in logging.root.manager.loggerDict]

    for logger_name in logger_name_list:
        # 获取当前 logger 的日志级别
        effective_level = logging.getLogger(logger_name).getEffectiveLevel()
        # 设置日志级别，只打印出级别大于等于INFO的日志
        if effective_level < logging.getLevelName(config.LOGGER_LEVEL.upper()):
            logging.getLogger(logger_name).setLevel(config.LOGGER_LEVEL.upper())
            # 为顶级 logger（名字中不含 . 的 logger）添加自定义的 InterceptHandler。首先清空它们的处理器列表，然后添加自定义的 InterceptHandler
        if '.' not in logger_name:
            logging.getLogger(logger_name).handlers = []
            logging.getLogger(logger_name).addHandler(InterceptHandler())
