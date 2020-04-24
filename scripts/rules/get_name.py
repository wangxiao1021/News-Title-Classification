#coding=utf-8
import re
p = re.compile("《(.*)》")
with open('./data/train.tsv', 'r') as f:
    with open('./data/train.tsv', 'r') as f1:
        for line in f.readlines():
            line= line.split('\t')
            if line[0] == '13':
                res = p.findall(line[2])
                if res:
                    s = res[0].decode('utf-8')
                    #encode('gb18030')
#.decode('ISO-8859-1').encode('utf-8')
                    #.encode('utf-8')
#decode('ISO-8859-1')
  #                  s='《'+s+'》'
                    print('《'+s.encode('utf-8')+'》')
                    #print(res[0].decode('ISO-8859-1'))               
#f1.write(res)
f.close()
f1.close()

