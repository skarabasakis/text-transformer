def transform(s):
    transformed = ''
    prev = ''

    for char in s:
        c = char.lower()
        if (c not in 'aeiouy') or (c == 'y' and not prev.isalpha()):
            transformed += char
        prev = c

    return transformed
