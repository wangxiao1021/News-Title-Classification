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

        line["label"] = label + 5 if label == 5 or label == 6 else label
        print json.dumps(line)
