
#coding=UTF-8
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')

files = sys.argv[1: ]
res_map = dict()
for file_name in files:
    with open(file_name, 'r') as file:
        index = 0
        for line in file:
            if index not in res_map:
                res_map[index] = []
            res_map[index].append(line.strip())
            index += 1

for i in range(len(res_map)):
    res_vec = res_map[i]
    most_common = Counter(res_vec).most_common(1)
    if most_common[0][1] == 1:
        print res_vec[0]
    else:
        print most_common[0][0]

