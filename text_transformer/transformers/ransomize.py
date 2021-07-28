import random

def transform(s):
    transformed = ''

    for char in s:
        if char.isalpha():
            transformed += random.choice([char.lower(), char.upper()])
        else:
            transformed += char

    return transformed
