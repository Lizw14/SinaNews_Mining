#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re
import thulac
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

def count_all():
	input_list = 'list/data_location/mycode/china_loc_list_full.txt'
	word_counts = make_dict(input_list)
	output_dir = './data/count/word_count_list.txt'
	for year in xrange(2002,2018):
#	for year in xrange(2002,2003):
		year = str(year)
		input_dir = './data/split/'+year+'/'
		save_dir = './data/count/'+year+'/'
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
						f_out = save_dir+label+'.txt'
						try:
#							count(label=label, output=f_out, input=f_in)
#							print(label)
							day_dict = read_dict(f_out)
							for key in word_counts.keys():
								if key in day_dict:
									word_counts[key][79+12*(int(year)-2002)+int(month)] += day_dict[key]
						except Exception as e:
							print 'ERROR: ', label, e.message
	
	for key in word_counts:
		for year in xrange(1,17):
			word_counts[key][year-1] = word_counts[key][79+12*year-11:79+12*year+1].sum()
			word_counts[key][15+4*year-3] = word_counts[key][79+12*year-11:79+12*year-8].sum()
			word_counts[key][15+4*year-2] = word_counts[key][79+12*year-8:79+12*year-5].sum()
			word_counts[key][15+4*year-1] = word_counts[key][79+12*year-5:79+12*year-2].sum()
			word_counts[key][15+4*year-0] = word_counts[key][79+12*year-2:79+12*year+1].sum()

#	word_counts = sorted(word_counts.items(),key = lambda x:x[1],reverse = True)
	f = open(output_dir, 'w')
	for k in word_counts:
		f.write(k+' '+array_2_str(word_counts[k][:16])+'\n')
	for k in word_counts:
		f.write(k+'\n')
		for year in xrange(1,17):
			f.write(str(2001+year)+' '+array_2_str(word_counts[k][15+4*year-3:15+4*year+1])+array_2_str(word_counts[k][79+12*year-11:79+12*year+1])+'\n')
	f.close()

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
		output_dict[word] = np.zeros(272, 'int')
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
