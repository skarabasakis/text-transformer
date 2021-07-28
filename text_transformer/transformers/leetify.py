CHAR_MAP = {
    'a': '4',
    'b': '8',
    'e': '3',
    'g': '9',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
}

SUFFIX_MAP = {
    's': 'z',
    'ed': "'d",
    'cker': 'x0r',
    'ckers': 'x0rz',
}

WORD_MAP = {
    'the': 't3h',
    'own': 'pwn',
    'cool': 'kewl',
    'elite': '1337',
    'newbie': 'n00b',
    'dude': 'd00d',
    'girl': 'gurl',
    'ok': 'kk',
    'you': 'u',
    'are': 'r',
    'why': 'y',
    'please': 'plz'
}

def transform_dict(d, f):
    return { f(k) : f(v) for k, v in d.items() }

CHAR_MAP = {
    **CHAR_MAP,
    **transform_dict(CHAR_MAP, str.upper)
}

SUFFIX_MAP = {
    **SUFFIX_MAP,
    **transform_dict(SUFFIX_MAP, str.upper)
}
SUFFIX_MAP_KEYS = sorted(SUFFIX_MAP.keys(), key=len, reverse=True)

WORD_MAP = {
    **WORD_MAP,
    **transform_dict(WORD_MAP, str.title),
    **transform_dict(WORD_MAP, str.upper)
}

def transform(s):
    transformed = ''

    for word in s.split():
        if word in WORD_MAP.keys():
            transformed += WORD_MAP[word]
        else:
            stem, suffix = split_suffix(word)
            if stem in WORD_MAP.keys():
                transformed += WORD_MAP[stem]
            else:
                for char in stem:
                    if char in CHAR_MAP.keys():
                        transformed += CHAR_MAP[char]
                    else:
                        transformed += char
            if suffix:
                transformed += SUFFIX_MAP[suffix]
        transformed += ' '

    return transformed[:-1]


def split_suffix(word):
    for suffix in SUFFIX_MAP_KEYS:
        if word.endswith(suffix):
            return (word[:-len(suffix)], suffix)

    return (word, None)
