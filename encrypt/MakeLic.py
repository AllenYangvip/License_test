#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 上午10:19
# @Author  : Allen Yang
# @Site    : 
# @File    : MakeLic.py
# @Software: PyCharm
# @E-mail  : yangjh@szkingdom.com

"""
Don't doubt why I use the ip and netmask to make the secret.
Because when use the system of all in the VM.
We unable to get the Physics machine's info.
So the users can move the vm-img to other VM.
What we can do?
And the vm-img is not changed.
But i think evenif the vm-img not changed,but the ip and netmaks was must be changed.
That's why i use ip and netmask to make the secret.
                                          -- Allen Yang
                                          3-19-2018
"""
from encrypt import main as my_encrypt
import random
import string
import time
import os

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
    print en_str
    return en_str


# make the Dirty data
result = "".join(random.sample(string.ascii_letters + string.digits, 60))


def main(file_name, msg):
    file_name += ".lic"
    BASE_PATH = os.path.abspath('..')
    file_path = os.path.join(BASE_PATH,"LicenseDIR",file_name)
    print file_path

    test = ""

    for n in msg.split(",")[:3]:
        print n
        test += "," + n_encode(n)
    print "真是信息第一次加密："
    print test
    test += "," +msg.split(",")[-1]
    print "添加主机标识："
    print test
    print "真是信息+主机标识第二次加密："
    enc = my_encrypt(test)
    print enc

    # write the license file
    with open(file_path,"w+") as f:
        for i in xrange(5):
            f.write("".join(random.sample(string.ascii_letters + string.digits, 60)))

        # write the truely values
        f.write(enc)
        for i in xrange(5):
            f.write("".join(random.sample(string.ascii_letters + string.digits, 60)))


if __name__ == '__main__':
    # 1:the start time
    # 2:the end time
    # 3:the host num
    # 4:the secret
    start_stmp = 1521422369
    end_stmp = 1524100769
    h_num = 66
    secret = "DkCb@lEf@h=uDkCb@lEf@h:n>"
    msg = ""
    msg +=  str(start_stmp)
    msg += "," + str(end_stmp)
    msg += "," + str(h_num)
    msg += "," + str(secret)
    main("szkingdom",msg)



