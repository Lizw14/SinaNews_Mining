#encoding=UTF-8
import urllib2
import sys
import os
import os.path as osp
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def craw_all():
	for year in xrange(2002,2018):
		year = str(year)
		save_dir = './data/initial/'+year+'/'
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
					f = open(save_dir+label+'.txt', 'w')
					try:
						crawer(label=label, output=f)
					except Exception as e:
						print 'ERROR: ', label, e.message
					f.close()


def crawer(label='20020101am', output=None):
	url = 'http://news.sina.com.cn/head/news'+label+'.shtml'
	index_page = urllib2.urlopen(url).read()
	soup = BeautifulSoup(index_page, "html.parser", from_encoding='gb18030')
	for news in soup.find_all('a'):
		output.write(news.text.encode('utf-8')+'\n')
	print 'DONE: ', label
#	news = soup.find('a')
#	output.write(news.text.encode('utf-8')+'\n')

def test_crawer():
	label='20020101am'
	f = open(label+'.txt', 'w')
	crawer(label=label, output=f)
	print 'done'
	f.close()

if __name__=='__main__':
#test_crawer()
	craw_all()
