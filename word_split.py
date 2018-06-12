#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re
import thulac
import jieba

reload(sys)
sys.setdefaultencoding('utf-8')

def split_all():

	lac = thulac.thulac(seg_only=True)
#jieba.load_userdict('user_dict.txt')
	
	for year in xrange(2002,2018):
#	for year in xrange(2002,2003):
		year = str(year)
		input_dir = './data/clean/'+year+'/'
		save_dir = './data/jieba_split/'+year+'/'
		if not osp.exists(save_dir):
			os.mkdir(save_dir)
		for month in xrange(1,13):
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
					f_out = save_dir+label+'.txt'
					f_in = input_dir+label+'.txt'
					try:
						#split(label=label, output=f_out, input=f_in, lac=lac)
						jieba_split(label=label, output=f_out, input=f_in)
					except Exception as e:
						print 'ERROR: ', label, e.message


def split(label='20020101am', output='20020101am_split.txt', \
		input='20020101am_clean.txt', lac = thulac.thulac(seg_only=True)):
#f_stopwords = open('./list/stop_words.txt','r')
#	stopwords = []
#	for line in f_stopwords.readlines():
#		stopwords.append(line.strip())
#	f_stopwords.close()
	lac.cut_f(input, output)
	print 'DONE: ', label

def jieba_split(label='20020101am', output='20020101am_jieba_split.txt', \
		input='20020101am_clean.txt'):
#f_stopwords = open('./list/stop_words.txt','r')
#	stopwords = []
#	for line in f_stopwords.readlines():
#		stopwords.append(line.strip())
#	f_stopwords.close()
	f_in = open(input, 'r')
	lines = f_in.readlines()
	f_in.close()
	f_out = open(output,'w')
	for line in lines:
		line = line.strip()
		f_out.write(' '.join(jieba.cut(line))+'\n')
		#f_out.write(' '.join(jieba.cut(line, cut_all=True))+'\n')
		#f_out.write(' '.join(jieba.cut_for_search(line))+'\n')
	f_out.close()
	print 'DONE: ', label

def test_spliter():
	label='20020101am'
	f = label+'_split.txt'
	f_in = label+'_clean.txt'
#split(label=label, output=f, input=f_in)
	jieba_split()
	print 'done'

if __name__=='__main__':
#	test_spliter()
	split_all()
