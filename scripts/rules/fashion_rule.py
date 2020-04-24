#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

import re

fashion_words = "时尚购物"
# pattern = re.compile(r'(满.*赠)|(满.*减)|(满.*送)')
with open(sys.argv[1], 'r') as file:
    index = 0
    for line in file:
        line = line.strip()
        if re.search(r'(满.*赠)|(满.*减)|(满.*送)|(满.*省)', line):
            print("%s\t%s" % (index, "时尚"))
        index += 1
