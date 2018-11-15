#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-19 上午9:49
# @Author  : Allen Yang
# @Site    : 
# @File    : decrypt.py
# @Software: PyCharm
# @E-mail  : allenyangvip@126.com
#

from Decregister import main as dec_reg,n_decode
from Crypto.Cipher import AES
import base64



# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32
# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length. This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '='
# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
# generate a random secret key
#secret = os.urandom(BLOCK_SIZE)
secret = pad(dec_reg())
# create a cipher object using the random secret
cipher = AES.new(secret)


def main(encoded):
    # decode the encoded string
    decoded = DecodeAES(cipher, encoded)
    print 'Decrypted string:', decoded
    print secret
    return decoded


if __name__ == '__main__':
    # de_str = "sBN+NzXMpRwAX9xR1DEpY6O5sd6IJBPgCxJvPIKphsDnkUA/kuf3s7e8xe7ekN8NVQNVbjMCWlWAhZg18NzgTA=="
    # main(de_str)
    import os
    BASE_PATH = os.path.abspath('..')
    file_path = os.path.join(BASE_PATH, "LicenseDIR", "szkingdom.lic")
    with open(file_path, 'r') as f:
        ture_str = f.read()[300:-300]
    print "truely data:"
    print ture_str

    true_data = main(ture_str).split(",")

    print true_data[:-1]
    test_b = []
    for i in true_data[:-1]:
        if i:
            test_b.append(int(n_decode(i)))
    print test_b


