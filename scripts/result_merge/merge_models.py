#coding=utf-8
import sys
import json
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')


ch2label = {u"财经": 0, u"彩票": 1, u"房产": 2, u"股票": 3, u"家居": 4, u"教育": 5,
            u"科技": 6, u"社会": 7, u"时尚": 8, u"时政": 9, u"体育": 10, u"星座": 11, u"游戏": 12, u"娱乐": 13}
label2ch = {}
for ch, i in ch2label.iteritems():
    label2ch[i] = ch

berts = dict()
with open(sys.argv[1], "r") as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        berts[index] = probs

final3 = dict()
with open(sys.argv[2], "r") as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        bert = berts[index]
        final3[index] = []
        for r, b in zip(probs, bert):
            final3[index].append(r + b)

final = dict()
with open(sys.argv[4], "r") as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        bert = final3[index]
        final[index] = []
        for r, b in zip(probs, bert):
            final[index].append(r + b)

final4 = dict()
with open(sys.argv[5], "r") as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        probs4 = final[index]
        final4[index] = []
        for e, f in zip(probs, probs4):
            final4[index].append(f+e)

final2 = dict()
with open(sys.argv[3], "r") as file:
    for line in file:
        line = json.loads(line.strip())
        index = line["index"]
        probs = line["probs"]
        label = line["label"]

        probs2 = final4[index]
        final2[index] = []
        for e, f in zip(probs, probs2):
            final2[index].append(f+e)
index = 0
for i in range(len(final2)):
    tmp_probs = final2[i]
    n_probs = np.array(tmp_probs)
    label = np.argmax(n_probs)
    print("%s\t%s\t%s" % (i, label2ch(label), tmp_probs))
    index += 1
