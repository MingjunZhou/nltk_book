import re, nltk


def compress(word):
    regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
    pieces = re.findall(regexp, word)
    return ''.join(pieces)


def stem(word):
    """Strips off anything that looks like a suffix."""
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

if __name__ == '__main__':
    english_udhr = nltk.corpus.udhr.words('English-Latin1')
    print nltk.tokenwrap(compress(w) for w in english_udhr[:75])
