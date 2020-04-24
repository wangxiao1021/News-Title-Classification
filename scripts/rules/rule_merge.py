#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

index_cate = dict()
with open(sys.argv[1], 'r') as file:
    for line in file:
        line = line.strip().split("\t")
        index = int(line[0])
        cate = line[1]
        index_cate[index] = cate

with open(sys.argv[2], 'r') as file:
    index = 0
    for line in file:
        if index in index_cate:
            print(index_cate[index])
        else:
            print(line.strip())
        index += 1
