import os
import eel
from text_transformer import transformers
from text_transformer.config import ROOT_DIR

@eel.expose
def get_transformers():
    return transformers.__all__

@eel.expose
def transform(text, transformer_name):
    return transformers.transform(text, transformer_name)

def run():
    eel.init(f'{ROOT_DIR}/data/webui')
    eel.start('index.html', port=9090)
