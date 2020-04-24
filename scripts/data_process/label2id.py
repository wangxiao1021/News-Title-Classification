#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

ch2label = {u"财经": 0, u"彩票": 1, u"房产": 2, u"股票": 3, u"家居": 4, u"教育": 5, u"科技": 6, u"社会": 7, u"时尚": 8, u"时政": 9, u"体育": 10, u"星座": 11, u"游戏": 12, u"娱乐": 13}

with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        line = line.split('\t')
        line = str(ch2label[line[0].encode('utf-8').decode('utf-8')])+u'\t'+line[1][:-1]
        print (line.encode('utf-8').decode('utf-8'))
        #print (str(ch2label[line[0]])+u'\t'+line[1].encode('utf-8').decode('utf-8'))
