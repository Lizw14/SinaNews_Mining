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
            count(label=label, output=label+'_count_search.txt', input=label+'_split_search.txt')
        print('DONE:', year)


def count(label='20020101am', output='20020101am_split.txt', \
        input='20020101am_clean.txt'):
#   f_stopwords = open('./list/stop_words.txt','r')
#   stopwords = []
#   for line in f_stopwords.readlines():
#       stopwords.append(line.strip())
#   f_stopwords.close()
    word_count = {}
    f_in = open(input, 'r')
    lines = f_in.readlines()
    f_in.close()
    word_list = []
    for line in lines:
        word_list = word_list + line.strip().split()
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    word_count = sorted(word_count.items(),key = lambda x:x[1],reverse = True)
    f_out = open(output, 'w')
    for char,cnt in word_count:
        f_out.write(char+' '+str(cnt)+'\n')
    f_out.close()
    print 'DONE: ', label

if __name__=='__main__':
    split_all()
