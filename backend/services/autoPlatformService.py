# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/10 10:31
import os.path
from config import config
import git
from loguru import logger
import paramiko

MODULES = {
    "srm": "app/srm",
    "sdsdata": "app/sdsdata",
    "disp": "app/disp",
    "user": "app/user",
    "sdsbasic": "sdsbasic"
}


def checkout_branch(task: dict) -> bool:
    """
    更新分支
    :param task: 模块与分支的对应关系，dict
    :return: bool
    """
    for module, branch in task.items():
        logger.info(f"module: {module}, branch: {branch}")
        if module in MODULES:
            module_path = os.path.join(config.BASE_ODP_DIR, MODULES[module])
            logger.info(f"module_path: {module_path}")
            try:
                repo = git.Repo(module_path)
                # 当前分支
                now_branch = repo.active_branch
                logger.info(f"module: {module}, now_branch: {now_branch}")
                # git checkout .
                repo.git.checkout('.')
                logger.info(f"module: {module}, checkout . success")
                # 如果要切换的分支，和当前分支一致，直接pull代码
                if now_branch == branch:
                    # git pull
                    repo.remotes.origin.pull()
                    logger.info(f"module: {module}, pull success")
                    return True
                # 如果不一致，先切到master，然后pull代码，最后切到对应分支
                # git checkout master
                repo.git.checkout(config.MASTER_BRANCH)
                logger.info(f"module: {module}, checkout master success")
                # git pull
                repo.remotes.origin.pull()
                logger.info(f"module: {module}, pull success")
                # git checkout branch
                repo.git.checkout(branch)
                logger.info(f"module: {module}, checkout {branch} success")
                after_branch = repo.active_branch
                logger.info(f"module: {module}, after_branch: {after_branch}")

            except git.exc.GitError as git_err:
                logger.error(f"checkout branch error: {git_err}")
                return False
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                return False
    return True


# def checkout_branch_remote(task):
#     """
#     远程更新分支
#     :param task:
#     :return: bool
#     """
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#
#     try:
#         client.connect(hostname=task.ip, username=task.username, password=task.password)
#         for module, branch in task.modules.items():
#             logger.info(f"module: {module}, target_branch: {branch}")
#         client.close()
#         return True
#     except paramiko.AuthenticationException:
#         return False


def callback(c):
    logger.info(f"task_id: {c.task_id}, status: {c.status}")
    return True
