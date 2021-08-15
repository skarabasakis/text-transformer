import eel
from text_transformer import transformers

@eel.expose
def get_transformers():
    return transformers.__all__

@eel.expose
def transform(text, transformer_name):
    return transformers.transform(text, transformer_name)

def run():
    eel.init('data/webui')
    eel.start('index.html', port=9090)
