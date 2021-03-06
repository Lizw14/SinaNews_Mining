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

    count_all = {}
    for prov in provs:
        for year in xrange(2002,2018):
            year = str(year)
            label = save_dir+year+'/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
            #print label
            year_dict = read_dict(label+'_all_count.txt')
            for key in year_dict:
                if key not in count_all:
                    count_all[key] = np.zeros(17, 'float')
                count_all[key][0] += year_dict[key]
                count_all[key][int(year)-2001] += year_dict[key]

    for prov in provs:
        loc_counts = make_dict(input_list_1)
        word_counts = {}
        for year in xrange(2002,2018):
            year = str(year)
            label = save_dir+year+'/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
            #print label
            year_dict = read_dict(label+'_all_count.txt')
            for key in loc_counts.keys():
                if key in year_dict:
                    loc_counts[key][0] += year_dict[key]
                    loc_counts[key][int(year)-2001] = year_dict[key]
            for key in year_dict:
                if key in word_counts:
                    word_counts[key] += year_dict[key]
                else:
                    word_counts[key] = year_dict[key]
        for key in loc_counts.keys():
            for i in xrange(0,13):
                if loc_counts[key][i] != 0:
                    loc_counts[key][i] /= count_all[key][i]
#        for key in word_counts.keys():
#            word_counts[key] /= count_all[key][0]
        print( prov)
        word_counts = sorted(word_counts.items(),key = lambda x:x[1],reverse = True)
        loc_counts = sorted(loc_counts.items(),key = lambda x:x[1][0],reverse = True)

        # _all_stop: all_count - stop_words
        f = open(save_dir+'all/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])+'_all_stop.txt', 'w')
        for k,v in word_counts:
            if k not in stop_words and len(k.decode())>1:
                f.write(k+' '+str(v)+'\n')
        f.close()

        ## _all_count: all_count(word, count)
        #f = open(save_dir+'all/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])+'_all_count.txt', 'w')
        #for k,v in word_counts:
        #    if k not in stop_words:
        #        f.write(k+' '+str(v)+'\n')
        #f.close()

        ## _all_count_list: [word_in_list, all_count, 16*year_count]
        #f_1 = open(save_dir+'all/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])+'_all_count_list.txt', 'w')
        #for k,v in loc_counts:
        #    f_1.write(k+' '+array_2_str(v)+'\n')
        #f_1.close()


    count_all = sorted(count_all.items(),key = lambda x:x[1][0],reverse = True)
    f_1 = open(save_dir+'all_count.txt', 'w')
    for k,v in count_all:
	if k not in stop_words:
            f_1.write(k+' '+array_2_str(v.astype('int'))+'\n')
    f_1.close()

def array_2_str(a):
    output = '['+' '.join([str(i) for i in list(a)])+']'
    return output

def make_dict(input_list = 'list/data_location/mycode/china_loc_list_full.txt'):
    f = open(input_list, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for line in lines:
        word = line.strip()
# 16*[year]+ 16*[4*seanson]+16*[12*month] 16+16*4+16*12=16*17=272
# [0:15] [16:19, ... , 76:79] [80:91, ... ,]
        output_dict[word] = np.zeros(17, 'int')
    return output_dict

def read_dict(input_file = '20020101am_count.txt'):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for line in lines:
        key,value = line.strip().split()
        value = int(value)
        output_dict[key] = value
    return output_dict

if __name__=='__main__':
    split_all()
