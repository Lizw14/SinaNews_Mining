#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup
import re
import thulac
import numpy as np
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

def count_all():
	input_list = 'list/data_location/mycode/china_prov_list_orig.txt'
	word_counts = make_dict(input_list)
	output_dir = './data/count/word_count_prov.txt'
	orig_counts = read_dict('./data/count/word_count_list.txt')
	for key in word_counts:
		key_ = key.decode('utf-8')
		word_counts[key] += orig_counts[key]
		if key_.endswith('自治区') \
			or key_.endswith('自治县') \
			or key_.endswith('自治州'):
			word_counts[key] += orig_counts[str(key_[:-3])]
		elif key_.endswith('特别行政区'):
			word_counts[key] += orig_counts[str(key_[:-5])]
		elif len(key_)>2 \
			and (key_.endswith('市') \
			or key_.endswith('区') \
			or key_.endswith('县') \
			or key_.endswith('省')):
			word_counts[key] += orig_counts[str(key_[:-1])]
		if key_.startswith('广西') \
			or key_.startswith('宁夏') \
			or key_.startswith('新疆'):
			word_counts[key] += orig_counts[str(key_[:2])]
			

#	word_counts = sorted(word_counts.items(),key = lambda x:x[1],reverse = True)
	f = open(output_dir, 'w')
	for k in word_counts:
		f.write(k+' '+str(word_counts[k].sum())+' '+array_2_str(word_counts[k])+'\n')
	f.close()

	f = open(output_dir[:-4]+'.csv', 'w')
	csvwriter = csv.writer(f)
	for k in word_counts:
		out = [k.decode('utf-8').encode('GB2312')]
		out.extend(word_counts[k])
		csvwriter.writerow(out)
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
		output_dict[word] = np.zeros(16, 'int')
	return output_dict

def read_dict(input_file = '/data/count/word_count_list.txt'):
	f = open(input_file, 'r')
	lines = f.readlines()
	f.close()
	output_dict = {}
	for line in lines[:6469]:
		try:
			key, value = line.split('[')
			key = str(key.strip().decode('utf-8'))
			value = value.strip().strip(']').split()
			value = np.array(value, dtype='int')
			output_dict[key] = value
		except:
			print line
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
