#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-16 上午10:14
# @Author  : Allen Yang
# @Site    : 
# @File    : encrypt.py
# @Software: PyCharm
# @E-mail  : yangjh@szkingdom.com

#
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
# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
# generate a random secret key
#secret = os.urandom(BLOCK_SIZE)


def main(en_str):
    # encode a string
    print
    secret = pad(en_str.split(",")[-1])
    # create a cipher object using the random secret
    cipher = AES.new(secret)
    encoded = EncodeAES(cipher,en_str)
    print 'Encrypted string:', encoded
    print secret
    return encoded


if __name__ == '__main__':
    en_str = """1521422369,1521422369,66,DkCb@lEf@h=uDkCb@lEf@h:n>"""
    main(en_str)