# coding=utf-8
import paddlepalm as palm
import json
from paddlepalm.distribute import gpu_dev_count
import sys
from evaluate import res_evaluate
from glob import glob

def pre(step):
    # configs
    max_seqlen = 256
    batch_size = 64
    num_epochs = 10
    lr = 5e-5
    weight_decay = 0.01
    vocab_path = './pretrain/BERT-zh-base/vocab.txt'

    train_file = './data/train.tsv'
    predict_file = './data/train.tsv'
    config = json.load(open('./pretrain/BERT-zh-base/bert_config.json'))
    input_dim = config['hidden_size']
    num_classes = 14
    dropout_prob = 0.1
    random_seed = 1
    step = step
    task_name = 'news'
    save_path = './outputs/'
    pred_output = './outputs-train/bert/'
    save_type = 'ckpt'
    print_steps = 10000
    pre_params = './pretrain/BERT-zh-base/params'

   
    # -----------------------  for prediction ----------------------- 

    # step 1-1: create readers for prediction
    #print('prepare to predict...')
    predict_cls_reader = palm.reader.ClassifyReader(vocab_path, max_seqlen, seed=random_seed, phase='predict')
    # step 1-2: load the training data
    predict_cls_reader.load_data(predict_file, batch_size)
    
    # step 2: create a backbone of the model to extract text features
    pred_bert = palm.backbone.BERT.from_config(config, phase='predict')

    # step 3: register the backbone in reader
    predict_cls_reader.register_with(pred_bert)
    
    # step 4: create the task output head
    trainer = palm.Trainer(task_name)
    cls_pred_head = palm.head.Classify(num_classes, input_dim, phase='predict')
    
    # step 5: build forward graph with backbone and task head
    trainer.build_predict_forward(pred_bert, cls_pred_head)
 
    # step 6: load checkpoint
    # model_path = './outputs/ckpt.step'+str(save_steps)
    model_path = step
#'./outputs/ckpt.step'+str(step)
    trainer.load_ckpt(model_path)

    # step 7: fit prepared reader and data
    trainer.fit_reader(predict_cls_reader, phase='predict')

    # step 8: predict
    #print('predicting..')
    trainer.predict(print_steps=print_steps, output_dir=pred_output)

    print('---------'+ str(step) + '----------')

if __name__ == '__main__':
    models = glob('./outputs-bert/30000')
    #+str(sys.argv[1]))
    for m in models:
        pre(m)
        #res_evaluate(res_dir="./outputs-bert/predict/predictions.json", eval_phase='dev')
