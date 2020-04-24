#  -*- coding: utf-8 -*-

import json
import numpy as np
import sys

def accuracy(preds, labels):
    preds = np.array(preds, dtype='float32')
    labels = np.array(labels, dtype='float32') 
    return (preds == labels).mean()

def pre_recall_f1(preds, labels, l):
    preds = np.array(preds)
    labels = np.array(labels)
    # recall=TP/(TP+FN)
    tp = np.sum((labels == l) & (preds == l))
    fp = np.sum((labels != l) & (preds == l))
    fn = np.sum((labels == l) & (preds != l))
    r = tp * 1.0 / (tp + fn)
    # Precision=TP/(TP+FP)
    p = tp * 1.0 / (tp + fp)
    epsilon = 1e-31
    f1 = 2 * p * r / (p+r+epsilon)
    return p, r, f1


def res_evaluate(res_dir="./outputs/predict/predictions.json", eval_phase='cu', data_dir=None):
    flag=0
    if data_dir:
        flag=1
    if eval_phase =='cu':
        flag=0
    elif eval_phase == 'test':
        data_dir="./data/test.tsv"
    elif eval_phase == 'dev':
        data_dir="./data/dev.tsv"
    elif eval_phase == 't':
        data_dir='./data/t.tsv'
    elif eval_phase == 'tid':
        data_dir='./data/test-id.tsv'
    else:
        assert eval_phase in ['dev', 'test'], 'eval_phase should be dev or test'
    
    labels = []
    with open(data_dir, "r") as file:
        first_flag = True
        for line in file:
            line = line.split("\t")
            label = line[flag]
            if label=='label':
                continue
            labels.append(str(label))
    file.close()

    preds = []
    with open(res_dir, "r") as file:
        for line in file.readlines():
            line = json.loads(line)
            pred = line['label']
            preds.append(str(pred))
    file.close()
    assert len(labels) == len(preds), "prediction result({}) doesn't match to labels ({})".format(len(preds),len(labels))
    print('data num: {}, accuracy: {:.4f}'.format(len(labels), accuracy(preds, labels)))
    for l in range(14):
        p, r, f1 = pre_recall_f1(preds, labels, str(l))
        print("label: {}, precision: {:.4f}, recall: {:.4f}, f1: {:.4f}".format(l,  p, r, f1))

#res_evaluate()
