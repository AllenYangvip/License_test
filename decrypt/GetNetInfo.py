#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 上午9:50
# @Author  : Allen Yang
# @Site    : 
# @File    : GetNetInfo.py
# @Software: PyCharm
# @E-mail  : allenyangvip@126.com


import os



def main():
    ip = []
    output = os.popen('ifconfig | grep inet | grep -v inet6 | grep -v 127.0.0.1')
    # print output.read().split()
    for i in output.readline().split():
        if i[-1].isdigit():
            # print i.split(":")[-1]
            ip.append(i.split(":")[-1])
    return ip[:2]

if __name__ == '__main__':
    print main()