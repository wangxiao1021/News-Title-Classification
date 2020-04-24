#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        if int(sys.argv[2]) == label:
            print index
