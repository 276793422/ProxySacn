'''
name: guajicun代理IP抓取
author: NemesisZoo
description:
'''


import requests
from lxml import etree
from Library.UserAgentRand import get_random_ua
from Library.MakeString import MakeStandardIpAddress
from Library.MakeString import MakeStandardPort
from Library.MakeString import MakeStandardProto


class GetProxyIP_GuaJiCunDaiLi:
    def __init__(self):
        self.url = 'http://proxy.guajicun.com/ProxyScanHTTPS%281%29.txt'

    def get_ip_file(self, url):
        list = []
        headers = {'User-Agent': get_random_ua()}
        html = requests.get(url=url, headers=headers, timeout=5).content.decode('utf-8', 'ignore')
        # 基准xpath，匹配每个代理IP的节点对象列表
        tr_list = html.split('\n')
        for tr in tr_list:
            ip = MakeStandardIpAddress(tr)
            https = 'http'
            list.append(https.lower() + '://' + ip)
            https = 'https'
            list.append(https.lower() + '://' + ip)

        return list

    # 主函数
    def Run(self):
        return self.get_ip_file(self.url)
