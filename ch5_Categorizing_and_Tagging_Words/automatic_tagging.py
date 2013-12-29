from nltk.corpus import brown
import nltk


def default_tagger(corpus):
    tags = [tag for (word, tag) in corpus.tagged_words(categories='news')]
    max_tag = nltk.FreqDist(tags).max()
    return nltk.DefaultTagger(max_tag)


def regexp_tagger():
    patterns = [(r'.*ing$', 'VBG'),               # gerunds
                (r'.*ed$', 'VBD'),                # simple past
                (r'.*es$', 'VBZ'),                # 3rd singular present
                (r'.*ould$', 'MD'),               # modals
                (r'.*\'s$', 'NN$'),               # possessive nouns
                (r'.*s$', 'NNS'),                 # plural nouns
                (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
                (r'.*', 'NN')                     # nouns (default)
                ]
    return nltk.RegexpTagger(patterns)


def lookup_tagger():
    fd = nltk.FreqDist(brown.words(categories='news'))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    most_freq_words = fd.keys()[:100]
    likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
    #return nltk.UnigramTagger(model=likely_tags)
    return nltk.UnigramTagger(model=likely_tags,
                              backoff=nltk.DefaultTagger('NN'))


def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))


def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
    
if __name__ == "__main__":
    raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
    tokens = nltk.word_tokenize(raw)
    tagger = default_tagger(brown)
    print tagger.tag(tokens)
    brown_tagged_sents = brown.tagged_sents(categories='news')
    print tagger.evaluate(brown_tagged_sents)
    brown_sents = brown.sents(categories='news')
    regtagger = regexp_tagger()
    print regtagger.tag(brown_sents[3])
    print regtagger.evaluate(brown_tagged_sents)
    baseline_tagger = lookup_tagger()
    print baseline_tagger.evaluate(brown_tagged_sents)
    sent = brown.sents(categories='news')[3]
    print baseline_tagger.tag(sent)

    display()
