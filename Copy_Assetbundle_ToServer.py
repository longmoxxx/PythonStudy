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
    os.system(cmd)

def Main():
    copy_file_to_server()
    pass


if __name__ == "__main__":
    Main()