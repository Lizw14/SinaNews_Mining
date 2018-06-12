# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import xml.etree.cElementTree as ET

xml_path = '../list.plist'
tree = ET.parse(xml_path)
root = tree.getroot()

loc = []
for name in root.iter('key'):
	loc.append(name.text[6:])
for name in root.iter('string'):
	loc.append(name.text[6:])

f = open('china_loc_list_orig.txt', 'w')
for name in loc:
	f.write(name.encode('utf-8')+'\n')
f.close()

f_all = open('china_loc_list_full.txt', 'w')
f_orig = open('china_loc_list_orig.txt', 'r')
for line in f_orig:
	line = line.strip().decode('utf-8')
	if line.endswith('自治区') \
			or line.endswith('自治县') \
			or line.endswith('自治州'):
		f_all.write(line[:-3]+'\n')
		print line[:-3]
	elif line.endswith('特别行政区'):
		f_all.write(line[:-5]+'\n')
		print line[:-5]
	elif len(line)>2 \
			and (line.endswith('市') \
			or line.endswith('区') \
			or line.endswith('县') \
			or line.endswith('省')):
		f_all.write(line[:-1]+'\n')
	f_all.write(line+'\n')

f_all.close()
f_orig.close()
