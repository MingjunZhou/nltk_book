import pprint, nltk

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
print text
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[171:181])
