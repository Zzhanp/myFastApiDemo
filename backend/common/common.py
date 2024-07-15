# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/10 16:14
import uuid
from pathlib import Path


def get_str_uuid():
    return str(uuid.uuid4()).replace("-", "")


def create_dir(file_name: str) -> Path:
    """ 创建文件夹 """
    path = Path(file_name).absolute().parent / file_name  # 拼接日志文件夹的路径
    if not Path(path).exists():  # 文件是否存在
        Path.mkdir(path)

    return path
