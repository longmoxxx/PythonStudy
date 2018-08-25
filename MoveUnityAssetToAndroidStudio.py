# -*- coding: utf-8 -*-
# 读写2007 excel
import os
import shutil

# 拷贝资源到服务器
def copy_file_to_server():
    src_path = 'E:/Git/TKXY_ClientTV_ChildrenTV/Assets/StreamingAssets/'
    dest_host = "192.168.120.96"
    dest_path = "/var/www/html/upgrade/box/Asset/"
    Window_to_Linux_Dir(src_path,dest_path,dest_host,"root",r"E:\key\putty_private.ppk")


def Window_to_Linux_Dir(window_path, Linux_path, Linux_ip, username, private_key):
    cmd = 'pscp -i {private_key} -r  {window_path} {username}@{Linux_ip}:{Linux_path}'.format(private_key=private_key,window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
    print(cmd)
    os.system(cmd)


# 删除文件及目录，exclude_files排除指定文件
def del_file(path,exclude_files):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        isfind = False
        for file in exclude_files:
            if c_path == file:
                isfind = True
                break
        if isfind:
            continue
        if os.path.isdir(c_path):
            shutil.rmtree(c_path)
        else:
            print(c_path)
            os.remove(c_path)

# 拷贝文件到Android Studio工程中
def MoveFile(unity_asset_path,android_data_path):
    android_exclude_files = (android_data_path + '\\nginx.crt',)
    del_file(android_data_path,android_exclude_files)
    for root, dirs, files in os.walk(unity_asset_path):
        for f in files:
            # 获取原始文件路径
            unity_file_path = os.path.join(root,f)
            #获取原始文件独立文件夹及路径
            temp_path = unity_file_path.replace(unity_asset_path+'\\',"")
            #Android工程文件路径
            android_path = os.path.join(android_data_path,temp_path)
            dir_name = os.path.dirname(android_path)
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
            shutil.move(unity_file_path,android_path)
    unity_exclude_files = ()
    del_file(unity_asset_path, unity_exclude_files)
def Main():
    # copy_file_to_server()
    unity_asset_path = r"C:\Users\HX\Desktop\TXKY_ClientTV_AndroidStudio\ChildrenTV\src\main\assets"
    android_data_path = r"E:\Git\HJH_box_reconstruct\app\src\main\assets"
    MoveFile(unity_asset_path,android_data_path)
    pass


if __name__ == "__main__":
    Main()