import eel
from text_transformer import transformers

@eel.expose
def get_transformers():
    return transformers.__all__

@eel.expose
def transform(text, transformer_name):
    return getattr(transformers, transformer_name)(text)

def run():
    eel.init('text_transformer/webui/web')
    eel.start('index.html', mode=None, port=9090)
