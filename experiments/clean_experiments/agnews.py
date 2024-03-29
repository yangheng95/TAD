# -*- coding: utf-8 -*-
# file: train_text_classification_bert.py
# time: 2021/8/5
# author: yangheng <yangheng@m.scnu.edu.cn>
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

from anonymous_demo import TextClassificationTrainer, ClassificationDatasetList, TCConfigManager, BERTTCModelList

classification_config_english = TCConfigManager.get_classification_config_english()
classification_config_english.model = BERTTCModelList.BERT
classification_config_english.num_epoch = 10
classification_config_english.evaluate_begin = 0
classification_config_english.pretrained_bert = 'bert-base-uncased'
classification_config_english.max_seq_len = 80
classification_config_english.log_step = -1
classification_config_english.dropout = 0.5
classification_config_english.cache_dataset = False
classification_config_english.seed = {42, 56, 1}
classification_config_english.l2reg = 1e-5
classification_config_english.learning_rate = 1e-5
classification_config_english.cross_validate_fold = -1

dataset = ClassificationDatasetList.AGNews10K
text_classifier = TextClassificationTrainer(config=classification_config_english,
                                            dataset=dataset,
                                            checkpoint_save_mode=1,
                                            auto_device=True
                                            ).load_trained_model()
