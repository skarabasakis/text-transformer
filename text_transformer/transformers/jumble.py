import random

def transform(s):
    transformed = ''

    for word in s.split():
        if len(word) <= 1:
            transformed += word + ' '
            continue

        first, middle, last = word[:1], word[1:-1], word[-1:]
        transformed += ''.join((first, *random.sample(middle, len(middle)), last, ' '))


    return transformed[:-1]
