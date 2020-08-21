'''
name: UA
author: NemesisZoo
description:
'''
from fake_useragent import UserAgent


# 随机生成User-Agent
def get_random_ua():
    ua = UserAgent()  # 创建User-Agent对象
    return ua.random
