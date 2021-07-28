import random
from text_transformer.transformers import jumble

def test_jumble():
    random.seed(0)

    original = '''According to a research at Cambridge University, it doesn't matter in what order the letters in
    a word are, the only important thing is that the first and last letter be at the right place. The rest can be a
    total mess and you can still read it without problem. This is because the human mind does not read every letter
    by itself but the word as a whole'''

    jumbled = '''Anriccodg to a reacresh at Cbmagride Uiyisvernt, it dns'oet mettar in what oedrr the lttrees in
    a word are, the only iotrmpnat tnihg is taht the fsrit and lsat lteter be at the rihgt palce. The rest can be a
    tatol mses and you can siltl read it whiuott poblrem. This is bseuace the hmuan mind does not read evrey letetr
    by itlesf but the word as a wlohe'''

    assert jumbled == jumble(original)
