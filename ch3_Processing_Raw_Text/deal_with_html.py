import nltk
from urllib import urlopen


def read_from_url(url, proxies=None):
    #proxies = {'http': 'http://127.0.0.1:8087'}
    raw = urlopen(url, proxies=proxies).read()
    return raw 

if __name__ == "__main__":
    url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
    html = read_from_url(url)
    raw = nltk.clean_html(html)
    tokens = nltk.word_tokenize(raw)
    tokens = tokens[96:399]
    text  = nltk.Text(tokens)
    print text.concordance('gene')
