# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys
from snownlp import SnowNLP
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

def sentiment_all():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    senti_dict = make_dict(input_list)
    senti_all_dict = make_dict(input_list)
    save_dir = './data/select_prov/'
    for year in xrange(2002,2018):
    #for year in xrange(2012,2018):
        year = str(year)
        for prov in provs:
            label = save_dir+year+'/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
            print label
            senti_all_dict[prov].append(sentiment_list(label+'_all.txt', label+'_all_senti.txt'))
            senti_dict[prov].append(sentiment_list(label+'.txt', label+'_senti.txt'))
        print('DONE:', year)

    f = open(save_dir+'senti.csv', 'w')
    csvwriter = csv.writer(f)
    for k in senti_dict:
        out = [k.decode('utf-8').encode('GB2312')]
        out.extend(senti_dict[k])
        csvwriter.writerow(out)
    f.close()

    f = open(save_dir+'senti_all.csv', 'w')
    csvwriter = csv.writer(f)
    for k in senti_all_dict:
        out = [k.decode('utf-8').encode('GB2312')]
        out.extend(senti_all_dict[k])
        csvwriter.writerow(out)
    f.close()

def make_dict(input_list = 'list/data_location/mycode/china_prov_list_simple.txt'):
    f = open(input_list, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for line in lines:
        output_dict[line.strip()] = []
    return output_dict

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
    sentiment_all()
