#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re
import thulac
import numpy as np
from snownlp import SnowNLP

reload(sys)
sys.setdefaultencoding('utf-8')

def count_all():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    for year in xrange(2002,2018):
#    for year in xrange(2002,2003):
        word_dict = make_dict(input_list)
        year = str(year)
        input_dir = './data/clean/'+year+'/'
        save_dir = './data/select_prov/'+year+'/'
        if not osp.exists(save_dir):
            os.mkdir(save_dir)
        for season in xrange(1,5):
            for month in xrange(3*season-2, 3*season+1):
                end_day = 30
                if month in [1,3,5,7,8,10,12]:
                    end_day = 31
                if month==2:
                    if year in [2004,2008,2012,2016]:
                        end_day = 29
                    else:
                        end_day = 28
                for day in xrange(1,end_day+1):
                    month = str(month).zfill(2)
                    day = str(day).zfill(2)
                    for time in ['am', 'pm']:
                        label = year+month+day+time
                        f_in = input_dir+label+'.txt'
                        try:
                            select(input=f_in, word_dict=word_dict, provs=provs)
                        except Exception as e:
                            print 'ERROR: ', label, e.message
                print ('DONE', year, month)
        for prov in provs:
            out_label = [str(i) for i in SnowNLP(unicode(prov)).pinyin]
            f_out = open(save_dir+''.join(out_label)+'_all.txt', 'w')
            f_out.write(list_2_str(word_dict[prov]))
            f_out.close()

def list_2_str(a):
    output = '\n'.join([str(i) for i in list(a)])
    return output

def make_dict(input_list = 'list/data_location/mycode/china_prov_list_simple.txt'):
    f = open(input_list, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for line in lines:
        output_dict[line.strip()] = []
    return output_dict


def select(input='sample/20020101am_clean.txt', \
            word_dict = make_dict('list/data_location/mycode/china_prov_list_simple.txt'), \
            provs = [prov.strip() for prov in (open('list/data_location/mycode/china_prov_list_simple.txt', 'r')).readlines()]):
    f_in = open(input, 'r')
    lines = f_in.readlines()
    f_in.close()
    lines = [line.strip() for line in lines]
    for line in lines:
        for prov in provs:
            if re.search(prov, line) != None:
                word_dict[prov].append(line)
                #if line not in word_dict[prov]:
                 #   word_dict[prov].append(line)

def test_selecter():
    word_dict = make_dict()
    select(word_dict=word_dict)
    f_out = open('sample/20020101am_select.txt', 'w')
    f_out.write(list_2_str(word_dict[word_dict.keys()[1]]))
    f_out.close()
    print 'done'

if __name__=='__main__':
    #test_selecter()
    count_all()
