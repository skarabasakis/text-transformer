from .silence import transform as silence
from .leetify import transform as leetify
from .jumble import transform as jumble
from .ransomize import transform as ransomize

__all__ = ['silence', 'leetify', 'jumble', 'ransomize']

def transform(text, transformer_name):
    return globals()[transformer_name](text)
