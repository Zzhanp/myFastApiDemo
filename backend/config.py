# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/10 15:06
from pydantic import BaseSettings


class Configs(BaseSettings):
    # logger
    LOGGER_DIR: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = 'qa_test_fast.log'  # 日志文件名  (时间格式 {time:YYYY-MM-DD_HH-mm-ss}.log)
    LOGGER_LEVEL: str = 'INFO'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "10 MB"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]
    # git
    MASTER_BRANCH: str = "master"
    BASE_ODP_DIR: str = "/home/sftcwl/odp_sds"

    class Config:
        case_sensitive = True  # 区分大小写
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Configs()