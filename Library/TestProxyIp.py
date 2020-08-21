'''
name: 代理验证
author: NemesisZoo
description:
'''
import requests

# test_url = 'http://httpbin.org/get'
# http 代理，访问http 的，https 代理访问https的
test_urld = 'http://api.ipify.org/'
test_urls = 'https://api.ipify.org/'


# 测试抓取的代理IP是否可用
def test_proxy_ip1(https, address):
    proxies = {https: address, }
    if https == 'http':
        test_url = test_urld
    elif https == 'https':
        test_url = test_urls
    else:
        return ''
    url = ''
    try:
        res = requests.get(url=test_url, proxies=proxies, timeout=8)
        if res.status_code == 200:
            string = str(res.content.decode("utf-8"))
            if address.find(string) != -1:
                # 包含，匿名
                url = '1|' + address
            else:
                # 不包含，返回IP不对，不匿名
                url = '0|' + address
            print(url + ' Success')
        else:
            print(address + ' Failed')
    except Exception as e:
        print(address + ' Errored')
    return url


# 测试抓取的代理IP是否可用
def test_proxy_ip2(https, ip, port):
    return test_proxy_ip1(https, https + '://' + ip + ':' + port)
