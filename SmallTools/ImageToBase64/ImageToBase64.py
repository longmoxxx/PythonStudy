# -*- coding: utf-8 -*-
# 将图片转换成base64字符串，以便Markdown工具存储

import os
import configparser
import base64

#获取文件路径，文件名称，文件后缀
def get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension

def read_file_write_to_ini(path):
    # 日志文件，在工程目录下。
    log_file = "image_base64_info.ini"
    config = configparser.ConfigParser()
    for root, dirs, files in os.walk(path):
        for f in files:
            file_exit_name = get_filePath_fileName_fileExt(f)[2]
            if file_exit_name == ".png" or file_exit_name == ".jpeg" or file_exit_name == ".jpg":
                fp = os.path.join(root, f)
                img = open(fp,'rb')
                ls_f = base64.b64encode(img.read())  # 读取文件内容，转换为base64编码
                img.close()
                config.add_section(fp)
                config.set(fp, "base64", str(ls_f))
    config.write(open(log_file, "w",encoding='UTF-8'))


def Main():
    read_file_write_to_ini(os.getcwd())
    pass


if __name__ == "__main__":
    Main()