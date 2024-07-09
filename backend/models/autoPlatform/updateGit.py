# -*- coding: utf-8 -*-            
# @Author : Zzhan
# @Time : 2024/7/9 19:59
import os.path
from common import commonResult
import git

BASE_DIR = "/home/sftcwl/odp_sds"
MODULES = {
    "srm": "app/srm",
    "sdsdata": "app/sdsdata"
}


def checkout_branch(task):
    for module, branch in task.items():
        if module in MODULES:
            module_path = os.path.join(BASE_DIR, MODULES[module])
            try:
                repo = git.Repo(module_path)
                repo.git.checkout(branch)
            except Exception as e:
                return commonResult.resp_400(message="更新失败")

    # try:
    #     repo = git.Repo(BASE_DIR)
    #     repo.git.checkout(branch)
    #
    # except Exception as e:
    #     return {"status": 0, "msg": "git clone error"}
