from text_transformer.transformers import leetify

def test_leetify():
    assert "5h0u71n9 fr0m t3h 70p 0f my lun9z" == leetify("shouting from the top of my lungs")

def test_leetify_with_custom_suffix():
    assert "h4x0rz pwn t3h n00bz" == leetify("hackers own the newbies")

def test_leetify_when_phrase_is_mixed_case():
    assert "M1x3d C453 L3773rZ R 1337" == leetify("MixEd CaSE LeTtErS Are Elite")

def test_leetify_when_custom_word_is_mixed_case():
    assert "Kewl H4x0rz R N3v3r PWN'D" == leetify("Cool Hackers Are Never OWNED")
