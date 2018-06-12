# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys
from snownlp import SnowNLP
import csv
import re
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

def split_all():
    input_list_1 = 'list/data_location/mycode/china_loc_list_full.txt'
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    f = open('./list/stop_words.txt', 'r')
    stop_words = f.readlines()
    f.close()
    stop_words = [i.strip() for i in stop_words]

    count_all = []
    for year in xrange(2002,2018):
        count_year = []
        for prov in provs:
            year = str(year)
            label = save_dir+year+'/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
            #print label
            f = open(label+'.txt', 'r')
            lines = f.readlines()
            count_year.extend(lines)
            f.close()
        count_all.extend(count_year)
        f = open(save_dir+str(year)+'/all.txt', 'w')
        for line in count_year:
            f.write(line)
        f.close()

    f = open(save_dir+'all.txt', 'w')
    for line in count_all:
        f.write(line)
    f.close()


if __name__=='__main__':
    split_all()
