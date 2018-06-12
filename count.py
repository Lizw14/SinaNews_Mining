#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re
import thulac

reload(sys)
sys.setdefaultencoding('utf-8')

def count_all():
	word_counts = {}
	output_dir = './data/count/word_count.txt'
	for year in xrange(2002,2018):
#	for year in xrange(2002,2003):
		year = str(year)
		input_dir = './data/jieba_split/'+year+'/'
		save_dir = './data/count/'+year+'/'
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
					f_in = input_dir+label+'.txt'
					f_out = save_dir+label+'.txt'
					try:
						count(label=label, output=f_out, input=f_in)
						f_count = open(f_out, 'r')
						lines = f_count.readlines()
						f_count.close()
						for line in lines:
							key,value = line.strip().split()
							value = int(value)
							if key in word_counts:
								word_counts[key] += value
							else:
								word_counts[key] = value
					except Exception as e:
						print 'ERROR: ', label, e.message
	word_counts = sorted(word_counts.items(),key = lambda x:x[1],reverse = True)
	f = open(output_dir, 'w')
	for k,v in word_counts:
		f.write(k+' '+str(v)+'\n')
	f.close()

def count(label='20020101am', output='20020101am_split.txt', \
		input='20020101am_clean.txt'):
#	f_stopwords = open('./list/stop_words.txt','r')
#	stopwords = []
#	for line in f_stopwords.readlines():
#		stopwords.append(line.strip())
#	f_stopwords.close()
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

def test_counter():
	label='20020101am'
	f = label+'_count.txt'
	f_in = label+'_split.txt'
	count(label=label, output=f, input=f_in)
	print 'done'

if __name__=='__main__':
#	test_counter()
	count_all()
