'''
name: 字符串处理
author: NemesisZoo
description:
'''


def RemoveChars(string):
    return string.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').replace('\'', '').replace('"',
                                                                                                                   '')


def MakeStandardIpAddress(string):
    return RemoveChars(string)


def MakeStandardPort(string):
    return RemoveChars(string)


def MakeStandardProto(string):
    return RemoveChars(string)
