# -*- coding: utf-8 -*-
import uuid


def creat_uuid():
    for index in  range(0,25): #读取一行
        print(str(uuid.uuid1()).replace('-',''))
def Main():
    creat_uuid()
    pass


if __name__ == "__main__":
    Main()