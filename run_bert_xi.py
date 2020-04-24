# coding=utf-8
import paddlepalm as palm
import json
from paddlepalm.distribute import gpu_dev_count


if __name__ == '__main__':

    # configs
    max_seqlen = 256
    batch_size = 64
    num_epochs = 2
    lr = 1e-6
    weight_decay = 0.0
    vocab_path = './pretrain/BERT-zh-base/vocab.txt'

    save_path = './outputs-bert-xi-4/'  #1111111111111
    train_file = './data/xidata/label4.tsv'#11111111111
    predict_file = './data/t.tsv'
    config = json.load(open('./pretrain/BERT-zh-base/bert_config.json'))
    input_dim = config['hidden_size']
    num_classes = 2
    dropout_prob = 0.0
    random_seed = 1
    task_name = 'news'
    save_type = 'ckpt'
    print_steps = 5
    pre_params = './pretrain/BERT-zh-base/params'

    # -----------------------  for training ----------------------- 

    # step 1-1: create readers for training
    cls_reader = palm.reader.ClassifyReader(vocab_path, max_seqlen, seed=random_seed, lang='cn')
    # step 1-2: load the training data
    cls_reader.load_data(train_file, batch_size, num_epochs=num_epochs)

    # step 2: create a backbone of the model to extract text features
    bert = palm.backbone.BERT.from_config(config)

    # step 3: register the backbone in reader
    cls_reader.register_with(bert)

    # step 4: create the task output head
    cls_head = palm.head.Classify(num_classes, input_dim, dropout_prob)

    # step 5-1: create a task trainer
    trainer = palm.Trainer(task_name)
    # step 5-2: build forward graph with backbone and task head
    loss_var = trainer.build_forward(bert, cls_head)

    # step 6-1*: use warmup
    n_steps = cls_reader.num_examples * num_epochs // batch_size
    warmup_steps = int(0.1 * n_steps)
    sched = palm.lr_sched.TriangularSchedualer(warmup_steps, n_steps)
    # step 6-2: create a optimizer
    adam = palm.optimizer.Adam(loss_var, lr)
    # step 6-3: build backward
    trainer.build_backward(optimizer=adam, weight_decay=weight_decay)
  
    # step 7: fit prepared reader and data
    trainer.fit_reader(cls_reader)
    
    # step 8-1*: load pretrained parameters
    trainer.load_pretrain(pre_params)
    # step 8-2*: set saver to save model
    # save_steps = n_steps 
    save_steps = 200
    trainer.set_saver(save_steps=save_steps, save_path=save_path, save_type=save_type)
    # step 8-3: start training
    trainer.train(print_steps=print_steps)
   
