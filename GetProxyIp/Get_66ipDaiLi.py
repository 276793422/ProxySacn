'''
name: 66ip代理IP抓取
author: NemesisZoo
description:
'''


import requests
from lxml import etree
from Library.UserAgentRand import get_random_ua
from Library.MakeString import MakeStandardIpAddress
from Library.MakeString import MakeStandardPort
from Library.MakeString import MakeStandardProto


class GetProxyIP_66ipDaiLi:
    def __init__(self):
        self.url = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=2&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip'

    def get_ip_file(self, url):
        list = []
        headers = {'User-Agent': get_random_ua()}
        html = requests.get(url=url, headers=headers, timeout=5).content.decode('utf-8', 'ignore')
        html = html.split('</script>')[2].split('</div>',1)[0]
        # 基准xpath，匹配每个代理IP的节点对象列表
        tr_list = html.split('<br />')
        for tr in tr_list:
            ip = MakeStandardIpAddress(tr)
            https = 'http'
            list.append(https.lower() + '://' + ip)
            https = 'https'
            list.append(https.lower() + '://' + ip)

        return list

    # 主函数
    def Run(self):
        list = []
        url2 = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=2&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip'
        list.extend(self.get_ip_file(url2))
        url3 = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip'
        list.extend(self.get_ip_file(url3))
        url4 = 'http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip'
        list.extend(self.get_ip_file(url4))
        return list
