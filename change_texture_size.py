from PIL import Image
import os
import sys
import configparser


# 获取文件后缀
def file_extension(path):
    return os.path.splitext(path)[1]

# 获取图片类型
#file_meta_path：meta文件路径
def get_texture_type(file_meta_path):
    file = open(file_meta_path, "r")
    for line in file.readlines():
        line_text = line.split(":")
        if line_text[0].strip() == "textureType":
            textureType = line_text[1].strip()
            return  textureType
    return "-1"

# 压缩图片
#scale：压缩比例
#path：压缩目录，root目录，会遍历所有子目录
def compress_image(scale,path):
    # 日志文件，在工程目录下。
    log_file = "compress_info.ini"
    if os.path.exists(sys.path[0]+"\\"+log_file):
        print("图片已经压缩过，如果要继续请删除compress_info.ini文件")
        return
    config = configparser.ConfigParser()
    for root, dirs, files in os.walk(path):
        for f in files:
            if file_extension(f) == ".png":
                fp = os.path.join(root, f)
                img = Image.open(fp)
                w, h = img.size
                new_w = int(w / scale)
                new_h = int(h / scale)
                # 文件长或宽小于1像素时不处理
                if new_w < 1 or new_h < 1:
                    continue
                file_meta = fp+'.meta'

                #判断是否存在meta文件
                if os.path.exists(file_meta):
                    textureType = get_texture_type(file_meta)
                    # 图片为sprite类型
                    if textureType == "8":
                        out_img = img.resize((new_w, new_h), Image.ANTIALIAS)
                        out_img.save(fp, "PNG")
                        config.add_section(fp)
                        config.set(fp, "原始尺寸", str(w)+"*"+str(h))
                        config.set(fp, "压缩尺寸", str(new_w) + "*" + str(new_h))
    config.write(open(log_file, "w",encoding='UTF-8'))


def Main():
    width_1 = 1920
    width_2 = 1280
    scale = width_1 / width_2
    # path = "E:/SVN/SmallPlayer/TKXY_ClientTV_Unity5.5.2_ChildrenTV/Assets"
    path = r"G:\\image"
    compress_image(scale,path)
    pass


if __name__ == "__main__":
    Main()