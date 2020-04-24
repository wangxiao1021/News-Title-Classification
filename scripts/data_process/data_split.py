#coding=utf-8
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
cu0 = []
cu1 = []
cu2 = []
cu3 = []
cu4 = []
cu5 = []
cu6 = []


with open('./data/test-id.tsv', 'r', encoding='utf-8' ) as fdata:
    if True:
    #with open('./data/train-cu.tsv','w' , encoding='utf-8') as fmerge:
        for data  in fdata.readlines():
            da = data[:-1]
            da = da.split('\t')   # label 0 cls 1 text 2
            label = da[0]
            if label == 'label':
                continue
            cu = -1
            if label == '8' or label == '12' or label == '13':
                if label =='8': 
                    label = '2'
                if label == '12':
                    label = '0'
                if label =='13':
                    label = '1'
                cu = 0
                cu0.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
            elif label == '0' or label == '1' or label == '3':
            
                if label =='3':
                    label = '2'
                cu = 1
                cu1.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
                #cu1.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
            elif label == '7' or label == '9':
                if label == '7':
                    label = '0'
                else:
                    label ='1'
                cu = 2
                cu2.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
                #cu2.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
            elif label == '2' or label == '4':
                cu = 3
                if label == '4':
                    label = '0'
                else:
                    label ='1'
                cu3.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
                #cu3.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
            elif label == '5' or label == '6':
                cu = 4
                if label == '6':
                    label = '0'
                else:
                    label ='1'
                cu4.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
#                cu4.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
            elif label == '10':
                cu = 5
                cu5.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
                #cu5.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
            elif label == '11':
                cu = 6
                cu6.append(str(cu)+'\t'+ label.encode('utf-8').decode('utf-8')+'\t'+da[1].encode('utf-8').decode('utf-8')[:-1])
                #cu6.append(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])

                
            #print(str(cu)+'\t'+ data.encode('utf-8').decode('utf-8')[:-1])
        print('culabel\tlabel\ttext_a')
        for i in cu6:
            print(i)
fdata.close()
#fmerge.close()
