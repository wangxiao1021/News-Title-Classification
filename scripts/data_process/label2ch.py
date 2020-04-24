#coding=UTF-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

ch2label = {u"财经": 0, u"彩票": 1, u"房产": 2, u"股票": 3, u"家居": 4, u"教育": 5, u"科技": 6, u"社会": 7, u"时尚": 8, u"时政": 9, u"体育": 10, u"星座": 11, u"游戏": 12, u"娱乐": 13}
label2ch = {}
for ch, i in ch2label.iteritems():
    label2ch[i] = ch

for line in sys.stdin:
    line = json.loads(line.strip())
    print label2ch[line['label']]
