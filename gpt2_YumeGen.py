# -*- coding: utf-8 -*-
"""GPT-2 Yume 1.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/176rafm3XUL3x9ljj_6VxfdHBpRSdtqO-
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
import tensorflow as tf

!pip install gpt-2-simple

import gpt_2_simple as gpt2_simple
from datetime import datetime

gpt2_simple.download_gpt2(model_name='124M') # Will take sometime....

from google.colab import files
gpt2_simple.mount_gdrive()

tf.reset_default_graph()
sess = gpt2_simple.start_tf_sess()

gpt2_simple.finetune(sess, dataset="/content/dreams.txt", steps=1000, model_name='124M',
                     sample_every=1000, save_every=5000, print_every=10, restore_from='fresh')
# This will take time. ignore the warning

# It generated dreamBank style text. the tiny dreambank dataset is a list of shake speare plays.
gpt2_simple.copy_checkpoint_to_gdrive(run_name='run1')

# gpt2_simple.copy_checkpoint_from_gdrive(run_name='run1')
# gpt2_simple.load_gpt2(sess,run_name='run1')

gpt2_simple.generate(sess, run_name='run1', prefix = "The secret of life is",nsamples = 5, length=100)