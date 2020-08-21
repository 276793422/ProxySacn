'''
name: 入口
author: NemesisZoo
description:
'''
from multiprocessing.dummy import Pool as ThreadPool

from Library.VersionInfo import PrintLogo

from GetProxyIp.Get_KuaiDaiLi import GetProxyIP_KuaiDaiLi
from GetProxyIp.Get_ZhiLianDaiLi import GetProxyIP_ZhiLianDaiLi
from GetProxyIp.Get_89ipDaiLi import GetProxyIP_89ipDaiLi
from GetProxyIp.Get_GuaJiCunDaiLi import GetProxyIP_GuaJiCunDaiLi
from GetProxyIp.Get_66ipDaiLi import GetProxyIP_66ipDaiLi
from Library.TestProxyIp import test_proxy_ip1
from Library.TestProxyIp import test_proxy_ip2


def GetAllProxy():
    list_proxy = []
    list_proxy.extend(GetProxyIP_KuaiDaiLi().Run())
    list_proxy.extend(GetProxyIP_ZhiLianDaiLi().Run())
    list_proxy.extend(GetProxyIP_89ipDaiLi().Run())
    list_proxy.extend(GetProxyIP_GuaJiCunDaiLi().Run())
    list_proxy.extend(GetProxyIP_66ipDaiLi().Run())

    return list_proxy


# 线程数量
threads_num = 10
# 并行任务池
test_thread_pool = ThreadPool(threads_num)

list_success = []


def test_thread(url):
    https = url.split(':', 1)[0]
    httpurl = test_proxy_ip1(https, url)
    if httpurl != '':
        list_success.append(httpurl)


def Start():
    list_proxy = GetAllProxy()

    print("共收集到代理IP ： [" + str(len(list_proxy)) + "]条")

    # 测试地址是否可用，这里用10个线程一直跑
    test_thread_pool.map(test_thread, list_proxy)

    print('success url : \n')
    for url in list_success:
        print(url)
        with open('out/proxies.txt', 'a') as f:
            f.write(url + '\n')


ut_list = [
]


def Test():
    # test_thread('https://58.220.95.55:9400')
    test_thread_pool.map(test_thread, ut_list)


if __name__ == '__main__':
    PrintLogo()
    #  burp 的单机代理测试，证明有效
    # test_proxy_ip1('http', 'http://127.0.0.1:8080')
    # test_proxy_ip1('https', 'https://58.255.206.135:34518')
    # Test()
    Start()




