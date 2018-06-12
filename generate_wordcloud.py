#!/usr/bin/env python
# -*- coding:utf-8 -*-

#引入需要的模块
# pip install Pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

prov = 'heilongjiang'

def read_dict(input_file = '/data/count/word_count_list.txt'):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for line in lines:
        try:
            key, value = line.strip().split()
            key = unicode(key.decode('utf-8'))
            value = int(value)
            output_dict[key] = value
        except:
            print line
    return output_dict

#inputlist = [(u'中国', 5), (u'环境', 4), (u'环保部', 3), (u'通知', 2), (u'健康', 1)]
#inputlist = dict(inputlist)
inputlist = read_dict('./data/select_prov/all/'+prov+'_wordcloud.txt')


#读入mask文件
#mask_image = np.array(Image.open("./mask.png"))
#调用WordCloud生成wordcloud
wordcloud = WordCloud(font_path='./list/FZLTCXHK-GBK1-0.otf', #字体文件路径
                      width=1000, #生成词云的宽度
                      height=500, #生成词云的高度
                      max_words=1000, #词云中最大量的词数
                      background_color='white' #生成的图片的背景颜色
                      ).generate_from_frequencies(inputlist)

#                      mask=mask_image, #使用的mask文件,此项不设置,默认生成矩形词云

#将生成的wordcloud图片保存在本地
wordcloud.to_file('./data/select_prov/wordcloud/'+prov+'.png')

#将生成的wordcloud图片打开显示出来
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()

