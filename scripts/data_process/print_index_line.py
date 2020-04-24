#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

index_set = set()
with open(sys.argv[2], 'r') as file:
    for line in file:
        index_set.add(int(line.strip()))

with open(sys.argv[1], 'r') as file:
    index = 0
    for line in file:
        line = line.strip()
        if index in index_set:
            print line
        index += 1
