from text_transformer.transformers import silence

def test_silence():
    assert "shtng frm th tp f hs lngs" == silence("shouting from the top of his lungs")

def test_silence_when_y_is_consonant():
    assert "rd lrr yllw lrr" == silence("red lorry yellow lorry")

def test_silence_when_phrase_starts_with_y():
    assert "yllw lrr"  == silence("yellow lorry")

def test_silence_when_phrase_is_mixed_case():
    assert "SHTNG Wth Mxd CS LTtrS" == silence("SHOUTING With MixEd CaSE LeTtErS")
