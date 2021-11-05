
import os
import sys
import easyocr

pic_path = '/mnt/0/dataset/1635934965813/'
p = os.listdir(pic_path)[0]


reader = easyocr.Reader(['ch_sim', 'en'], download_enabled=False)
result = reader.readtext(pic_path+p)
for line in result:
    print(line)


