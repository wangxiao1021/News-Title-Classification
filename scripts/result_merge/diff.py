#coding=utf-8
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# 查看results之间的diff
with open('merge_re', 'r' ) as f2:
    with open('youxi-trans', 'r') as f1:
        c = 1;
        for i,j in zip(f1.readlines(), f2.readlines()):
            if i!=j:
                print(c, i.encode('utf-8').decode('utf-8')[:-1], j.encode('utf-8').decode('utf-8')[:-1], j.encode('utf-8').decode('utf-8')[:-1])
            c+=1
f1.close()
f2.close()
