# -*- coding: utf-8 -*-
# 读写2007 excel
import openpyxl
import uuid
import os
import shutil

def file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_name(file_path):
    return os.path.splitext(file_path)[0]

def readExcel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.get_sheet_by_name("Sheet1")
    for row in sheet.rows: #读取一行
        file_path = str(row[0].value.strip()) #获取Excel表中视频路径
        if os.path.exists(file_path):
            try:
                file_uuid = str(uuid.uuid1()).replace('-', '')  # 生成uuid
                uuid_name = file_uuid + str(file_extension(file_path))
                row[2].value = uuid_name  # 修改Excel中UUID值，带后缀
                move_dir_name = "F:\\finished\\" + uuid_name
                shutil.move(file_path, move_dir_name)
            except Exception as e:
                print(e)
                break
    wb.save("hx_"+path)
def Main():
    file_name = 'video.xlsx'
    readExcel(file_name)
    pass


if __name__ == "__main__":
    Main()