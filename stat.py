#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re

reload(sys)
sys.setdefaultencoding('utf-8')

def clean_all():
    all_cnt = 0
    clean_cnt = 0
    for year in xrange(2002,2018):
#    for year in xrange(2002,2003):
        year_cnt = 0
        year_all_cnt = 0
        year = str(year)
        input_dir = './data/initial/'+year+'/'
        save_dir = './data/clean/'+year+'/'
        if not osp.exists(save_dir):
            os.mkdir(save_dir)
        for month in xrange(1,13):
            month_news = []
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
                    f_in = open(input_dir+label+'.txt', 'r')
                    lines = f_in.readlines()
                    f_in.close()
                    year_all_cnt += len(lines)
                    all_cnt += len(lines)
                    f = open(save_dir+label+'.txt', 'r')
                    lines = f.readlines()
                    f.close()
                    #lines_ = []
                    #for line in lines:
                    #    if line not in month_news:
                    #        lines_.append(line)
                    #month_news.extend(lines_)
                    year_cnt += len(lines)
        clean_cnt += year_cnt
        print(year, year_cnt)
        print(year,'all', year_all_cnt)
    print('ALL:', all_cnt)
    print('CLEAN:', clean_cnt)


def cleaner(label='20020101am', output=None, lines=[]):
    f_exclude = open('./list/exclude_gt4.txt','r')
    exclude_lists = []
    for line in f_exclude.readlines():
        exclude_lists.append(line.strip())
    f_exclude.close()
    for line in lines:
        line = line.strip()
        line = line.decode('utf-8')
#'全部 >>'
#and line.endswith('回顾')==False 
#'图片 回顾 地区新闻 更多专题'
#新闻网
#教育新闻排行
#[体育新闻]
        if len(line)>4 \
            and (line.startswith(' ')==False) \
            and (line.endswith('>>')==False) \
            and (len(re.findall(' ', line))<4) \
            and (line.endswith('新闻网')==False) \
            and (line.endswith('新闻排行')==False) \
            and ((line.startswith('[') and line.endswith(']'))==False) \
            and (line not in exclude_lists):
            line = re.sub('\(\S\S\)', '\n', line) #delete '(组图)'
            line = re.sub('\(\S\)', '\n', line) #delete '(图)'
            line = re.sub('\(\d\d\:\d\d\)', '\n', line) #delete '(12:08)'
            line = line.strip()
            output.write(line.encode('utf-8')+'\n')
    print 'DONE: ', label
#    news = soup.find('a')
#    output.write(news.text.encode('utf-8')+'\n')

def test_cleaner():
    label='20020101am'
    f = open(label+'_clean.txt', 'w')
    f_in = open(label+'.txt', 'r')
    lines = f_in.readlines()
    f_in.close()
    cleaner(label=label, output=f, lines=lines)
    print 'done'
    f.close()

if __name__=='__main__':
#test_cleaner()
    clean_all()
