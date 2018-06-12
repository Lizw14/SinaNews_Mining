# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import sys
from snownlp import SnowNLP
import csv
import re
import numpy as np

reload(sys)
sys.setdefaultencoding('utf-8')

def prov_year_class(prov_index=0):
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    npy = np.load(save_dir+'word_bag.npy')
    bag_info = read_list_bag_info('./list/bag_info.txt')
    f_bag = open('./list/bag.txt', 'r')
    bag_list = f_bag.readlines()
    bag_list = [line.strip() for line in bag_list]
    f_bag.close()

    #f = open(save_dir+'prov_year_class/'+''.join([str(i) for i in SnowNLP(unicode(provs[prov_index])).pinyin])+'_year_class.csv', 'w')
    f = open(save_dir+'prov_year_class.csv', 'w')
    csvwriter = csv.writer(f)
    for prov_index in xrange(34):
        row = [provs[prov_index], ' ']+[i[4] for i in bag_info]+bag_list
        row = [i.decode('utf-8').encode('GB2312') for i in row]
        csvwriter.writerow(row)
        for idx,year in enumerate(range(2002,2018)):
            #csvwriter.writerow([str(year)+'年'.decode('utf-8').encode('GB2312')]+list(npy[:,1000:1023,year-2001].sum(0)))
            csvwriter.writerow([str(year)+'年'.decode('utf-8').encode('GB2312')]+[npy[prov_index,1000:1023,year-2001].sum()*100/float(npy[:,1000:1023,year-2001].sum())]+list(npy[prov_index,1000:1023,year-2001])+list(npy[prov_index,:1000,year-2001]))
    f.close()
    print('prov_year_class Done')

def prov_year():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    npy = np.load(save_dir+'word_bag.npy')
    bag_info = read_list_bag_info('./list/bag_info.txt')
    f_bag = open('./list/bag.txt', 'r')
    bag_list = f_bag.readlines()
    bag_list = [line.strip() for line in bag_list]
    f_bag.close()

    f = open(save_dir+'prov_year.csv', 'w')
    csvwriter = csv.writer(f)
    row = [' ',' ']+[str(i)+'年' for i in range(2002,2018)]
    row = [i.decode('utf-8').encode('GB2312') for i in row]
    csvwriter.writerow(row)
    for idx,prov in enumerate(provs):
        #csvwriter.writerow([prov.decode('utf-8').encode('GB2312')]+list(npy[idx,1000:1023,0]))
        csvwriter.writerow([prov.decode('utf-8').encode('GB2312')]+list(npy[idx,1000:1023,:].sum(0)))
    f.close()
    print('prov_year Done')

def year_class():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    npy = np.load(save_dir+'word_bag.npy')
    bag_info = read_list_bag_info('./list/bag_info.txt')
    f_bag = open('./list/bag.txt', 'r')
    bag_list = f_bag.readlines()
    bag_list = [line.strip() for line in bag_list]
    f_bag.close()

    f = open(save_dir+'year_class.csv', 'w')
    csvwriter = csv.writer(f)
    row = [' ']+[i[4] for i in bag_info]+bag_list
    row = [i.decode('utf-8').encode('GB2312') for i in row]
    csvwriter.writerow(row)
    for idx,year in enumerate(range(2002,2018)):
        #csvwriter.writerow([str(year)+'年'.decode('utf-8').encode('GB2312')]+list(npy[:,1000:1023,year-2001].sum(0)))
        csvwriter.writerow([str(year)+'年'.decode('utf-8').encode('GB2312')]+list(npy[:,1000:1023,year-2001].sum(0))+list(npy[:,:1000,year-2001].sum(0)))
    f.close()
    print('year_class Done')

def prov_class():
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    npy = np.load(save_dir+'word_bag.npy')
    bag_info = read_list_bag_info('./list/bag_info.txt')
    f_bag = open('./list/bag.txt', 'r')
    bag_list = f_bag.readlines()
    bag_list = [line.strip() for line in bag_list]
    f_bag.close()

    f = open(save_dir+'prov_class.csv', 'w')
    csvwriter = csv.writer(f)
    row = [' ']+[i[4] for i in bag_info]+bag_list
    row = [i.decode('utf-8').encode('GB2312') for i in row]
    csvwriter.writerow(row)
    for idx,prov in enumerate(provs):
        #csvwriter.writerow([prov.decode('utf-8').encode('GB2312')]+list(npy[idx,1000:1023,0]))
        csvwriter.writerow([prov.decode('utf-8').encode('GB2312')]+list(npy[idx,1000:1023,0])+list(npy[idx,:1000,0]))
    f.close()
    print('word_class Done')

def word_bag_npy():
    input_list_1 = 'list/bag.txt'
    input_list = 'list/data_location/mycode/china_prov_list_simple.txt'
    f_in = open(input_list, 'r')
    provs = f_in.readlines()
    f_in.close()
    provs = [prov.strip() for prov in provs]
    save_dir = './data/select_prov/'

    npy = np.zeros([34,1023,17], 'int')
    bag_dict = make_dict(input_list_1)

    for idx, prov in enumerate(provs):
        label = save_dir+'all/'+''.join([str(i) for i in SnowNLP(unicode(prov)).pinyin])
        #print label
        year_dict = read_dict(label+'_count_search_bag.txt')
        for key in bag_dict.keys():
            npy[idx][key] = year_dict[bag_dict[key]]
        print( prov)

    #npy = npy.astype('float')
    bag_info = read_list_bag_info('./list/bag_info.txt')
    for line in bag_info:
        npy[:,1000+line[0],:] = (npy[:,line[1]:line[2]+1,:].sum(1)/float(line[3])*50).astype('int')

    np.save(save_dir+'word_bag.npy', npy)

def array_2_str(a):
    output = '['+' '.join([str(i) for i in list(a)])+']'
    return output

def make_dict(input_list = 'list/data_location/mycode/china_loc_list_full.txt'):
    f = open(input_list, 'r')
    lines = f.readlines()
    f.close()
    output_dict = {}
    for i in xrange(len(lines)):
        line = lines[i]
        word = line.strip()
        output_dict[i] = word
    return output_dict

def read_list_bag_info(input_file = './list/bag_info.txt'):
    f = open(input_file, 'r')
    lines = f.readlines()
    f.close()
    output_list = []
    for line in lines:
        line = line.strip().split()
        output_list.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), line[4]])
    return output_list

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

if __name__=='__main__':
    word_bag_npy()
    #prov_class()
    year_class()
    #prov_year_class()
    #prov_year()
