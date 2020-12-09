# !/usr/bin/python3

import random
import string
import json


ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'


def random_Value(len):
    """
    :param len: 随机码长度
    :return: 随机码数字字母组合
    """
    strV = ""
    # randVal = random.sample(ascii_uppercase + digits,len)
    # codeVal = strV.join(randVal)
    # return codeVal
    for a in range(len):
        index = random.randrange(0, len)
        if index >= a:
            strV += random.choice(ascii_uppercase)
        else:
            strV += random.choice(digits)
    return strV


def generateCode(codeLen, codeCount):
    """
    :param codeLen: 随机码长度
    :param codeCount: 随机码个数
    :return:
    """
    i = 0
    nlist = {}

    while i < codeCount:
        # number = random.randint(100,999)
        val = random_Value(codeLen)
        while val in nlist.values():
            # number = random.randint(100,999)
            val = random_Value(codeLen)
        # nlist[i] = number
        nlist[i] = val
        i += 1

    print(nlist)
    # print(json.dumps(nlist))


generateCode(6, 100)
