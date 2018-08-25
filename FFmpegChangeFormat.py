# -*- coding: utf-8 -*-
import os
import subprocess
import sys

#获取文件路径，文件名称，文件后缀
def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension


# -r:帧率，fps，例如：ffmpeg -i input.avi -r 30 output.mp4
#-b:比特率（比特率也是一个决定音视频总体质量的参数。他决定每个时间单位处理的bit数。）
#设置音视频整体比特率：ffmpeg -i file.avi -b 1.5M file.mp4
#设置音频比特率：ffmpeg -i input.avi -b:a 1500K output.mp4
#设置音频比特率：ffmpeg -i input.avi -b:v 1500K output.mp4
#CBR
#CBR设置一般用作直播流，比如视频会议。为输出设置CBR,有三个参数必须设置为同一个值。
#bitrate(-b option), minimal rate(-minrate), maximal rate(-maxrate)。maximal rate需要设置-bufsize选项。例如设置CBR为0.5Mbit/s。
#例如：ffmpeg -i in.avi -b 0.5M -minrate 0.5M -maxrate 0.5M -bufsize 1M output.mkv
def split_movie(input_video_path,output_video_path):
    #获取文件名称
    file_name = jwkj_get_filePath_fileName_fileExt(input_video_path)[1]
    #ffmpeg路径
    ffmpeg_path =  'E:/ffmpeg/ffmpeg-4.0.2-win64-shared/ffmpeg-4.0.2-win64-shared/bin/ffmpeg.exe -i '
    # 编码格式
    code_type=' -b:v 4M -minrate 4M -maxrate 4M -bufsize 4M ' \
              '-codec:v libx264 -codec:a mp3 -map 0 '
    #执行命令
    cmd=ffmpeg_path+input_video_path+code_type+output_video_path+'\\'+file_name+'.mp4'
    print(cmd)
    subprocess.call(cmd)

#遍历文件夹
def read_video_list(input_dir,output_dir):
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            file_exit_name =jwkj_get_filePath_fileName_fileExt(f)[2]
            if file_exit_name == ".mp4" or file_exit_name == ".mov"or \
                    file_exit_name == ".mpg"or file_exit_name == ".ts"\
                    or file_exit_name == ".mpeg":
                fp = os.path.join(root, f)
                split_movie(fp,output_dir)

def Main():
    #原视频路径
    input_dir ='F:\\finished\\'
    #输出视频路径
    output_dir = 'F:\\split\\'
    read_video_list(input_dir,output_dir)
    pass


if __name__ == "__main__":
    Main()