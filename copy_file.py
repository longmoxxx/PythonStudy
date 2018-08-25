# -*- coding: utf-8 -*-
# 读写2007 excel
import os
import shutil

def file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    return os.path.splitext(file_path)[0]

def copyfile(root_dir):
    i=0
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if file_extension(f) == ".mp4" or file_extension(f) == ".mov"or file_extension(f) == ".mpg"or file_extension(f) == ".ts":
                fp = os.path.join(root, f)
                new_file_path = "G:\\UUID\\"+f
                if os.path.exists(new_file_path):
                    i=i+1
                    shutil.move(fp, "F:\\copyed\\"+f)
                    print(i)
def Main():
    root_dir = "F:\\finish\\"
    copyfile(root_dir)
    pass


if __name__ == "__main__":
    Main()