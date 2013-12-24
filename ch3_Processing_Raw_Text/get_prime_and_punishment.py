import nltk, re, pprint
from urllib import urlopen


def read_from_url(url, proxies=None):
    #proxies = {'http': 'http://127.0.0.1:8087'}
    raw = urlopen(url, proxies=proxies).read()
    return raw 

def tokennize(raw):
    return nltk.word_tokenize(raw)

def find_contents(raw, start_string, end_string):
    beginning = raw.find(start_string)
    end = raw.rfind(end_string)
    raw = raw[beginning: end]
    return raw

if __name__ == "__main__":
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    raw = read_from_url(url)
    tokens = tokennize(raw)
    print tokens[:10]
    print len(tokens)
    
    text = nltk.Text(tokens)
    print type(text)
    print text[1020:1060]
    # find 20 sequences of words that occur together unusually ofen.
    text.collocations()
    
    raw = find_contents(raw, "PART I", "End of Project Gutenberg's Crime")
    print len(raw)
