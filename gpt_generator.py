import gpt_2_simple as gpt2
import numpy as np
from datetime import datetime
from gpt_scraper import file_name
from lista_respuestas import lista_gpt

gpt2.download_gpt2(model_name = '124M')
sess = gpt2.start_tf_sess()
gpt2.finetune(sess, file_name, steps=1000, 
              print_every = 10,
              sample_every = 500,
              run_name = 'run_1',
              save_every= 500)

# To load previous session
# gpt2.load_gpt2(sess, run_name = 'run_1')

gen_text = gpt2.generate(sess,
              length=200,
              temperature=0.7,
              prefix='<|startoftext|>',
              truncate='<|endoftext|>',
              include_prefix = False,
              return_as_list= True,
              nsamples=20,
              batch_size=20
              )

lista_gpt.append(gen_text)