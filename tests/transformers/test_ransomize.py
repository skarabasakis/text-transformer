import random
from text_transformer.transformers import ransomize

def test_ransomize():
    random.seed(0)
    assert "GIvE US TEN miLliOn DolLArS OR tHE PuppY gETs It!" == ransomize("give us ten million dollars or the puppy gets it!")
