#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 上午10:24
# @Author  : Allen Yang
# @Site    : 
# @File    : Decregister.py
# @Software: PyCharm
# @E-mail  : allenyangvip@126.com

from GetNetInfo import main as getnet
import random


def main():
    net = getnet()
    # print net
    dec_str = ''
    for ip in net:
        # print n_encode(ip)
        dec_str += n_encode(ip)
    print dec_str
    return dec_str
    # print "========================="
    # a = [1521422369,1521422369,66,"DkCb@lEf@h=uDkCb@lEf@h:n>"]
    # test = []
    # for n in a[:3]:
    #     test.append(n_encode(str(n)))
    # print test
    # print '+++++++++++++++++++++++++++++'
    #
    # nnn = ",DgCeCh?kAs,DgCh@f=oAs,Ih"
    # b = nnn.split(",")
    #
    # test_b = []
    # for k in b:
    #     if k:
    #         test_b.append(int(n_decode(k)))
    # print test_b




def n_decode(lst):
    de_str = ''
    num = 0
    for i in lst:
        num += 1
        if num % 2 == 0:
            char = chr(ord(i) - 48 - num)
        else:
            char = chr(ord(i) - 20 + num)
        de_str += char
    return de_str


def n_encode(lst):
    en_str = ''
    num = 0
    for i in lst:
        num += 1
        if num % 2 == 0:
            char = chr(ord(i) + 48 + num)
        else:
            char = chr(ord(i) + 20 - num)
        en_str += char
    return en_str


if __name__ == '__main__':
    main()