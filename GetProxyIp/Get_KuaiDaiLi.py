'''
name: 快代理，代理IP抓取
author: NemesisZoo
description:
'''


import requests
from lxml import etree
from Library.UserAgentRand import get_random_ua
from Library.MakeString import MakeStandardIpAddress
from Library.MakeString import MakeStandardPort
from Library.MakeString import MakeStandardProto


class GetProxyIP_KuaiDaiLi:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/'

    # 从快代理网站上获取随机的代理IP
    def get_ip_file(self, url):
        list = []
        headers = {'User-Agent': get_random_ua()}
        # 访问快代理网站国内高匿代理，找到所有的tr节点对象
        html = requests.get(url=url, headers=headers, timeout=5).content.decode('utf-8', 'ignore')
        parse_html = etree.HTML(html)
        # 基准xpath，匹配每个代理IP的节点对象列表
        tr_list = parse_html.xpath('//tr')
        for tr in tr_list[1:]:
            ip = MakeStandardIpAddress(tr.xpath('./td[1]/text()')[0])
            port = MakeStandardPort(tr.xpath('./td[2]/text()')[0])
            https = MakeStandardProto(tr.xpath('./td[4]/text()')[0])
            list.append(https.lower() + '://' + ip + ':' + port)

        return list

    # 主函数
    def Run(self):
        return self.get_ip_file(self.url)
