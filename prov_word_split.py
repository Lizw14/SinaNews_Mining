# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys
from snownlp import SnowNLP
import csv
import jieba
import thulac
import re

reload(sys)
sys.setdefaultencoding('utf-8')

def split_all():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'
    for year in xrange(2002,2018):
        year = str(year)
        for prov in provs:
            label = save_dir+year+'/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
            print label
            jieba_split(label=label, output=label+'_split_search.txt', input=label+'.txt')
        print('DONE:', year)


def jieba_split(label='20020101am', output='20020101am_jieba_split.txt', \
        input='20020101am_clean.txt'):
    f_in = open(input, 'r')
    lines = f_in.readlines()
    f_in.close()
    f_out = open(output,'w')
    for line in lines:
        line = line.strip()
        #f_out.write(' '.join(jieba.cut(line))+'\n')
        f_out.write(' '.join(jieba.cut_for_search(line))+'\n')
    f_out.close() 
    print 'DONE: ', label

def sentiment_list(list='sample/20020101am_clean.txt', \
        f_out = 'sample/20020101am_sentiment.txt'):
    f = open(list, 'r')
    lines = f.readlines()
    f.close()
    f_out = open(f_out, 'w')
    ave = 0
    for line in lines:
        line = line.strip()
        snow = SnowNLP(unicode(line))
        f_out.write(str(snow.sentiments)+' '+line+'\n')
        ave += snow.sentiments
    ave = ave/len(lines)
    f_out.write(str(ave))
    f_out.close()
    return ave

if __name__=='__main__':
    split_all()
