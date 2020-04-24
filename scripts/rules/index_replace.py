#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')


index_label_map = set()
ilabel = int(sys.argv[2])
with open(sys.argv[2], 'r') as file:
    for line in file:
        index_label_map.add(int(line.strip()))
    #for line in file:
     #   line = line.strip().split()
      #  index_label_map[int(line[0])] = int(line[1])

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        line["label"] = ilabel if index in index_label_map else label
        print json.dumps(line)
