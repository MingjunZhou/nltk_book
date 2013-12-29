from nltk.corpus import brown
import nltk


def unigram_tagging(tagged_corpus):
    return nltk.UnigramTagger(tagged_corpus)


def train_test(dataset, percent):
    size = int(len(dataset) * percent)
    train_sents = dataset[:size]
    test_sents = dataset[size:]
    return train_sents, test_sents


def bigram_tagging(tagged_corpus):
    return nltk.BigramTagger(tagged_corpus)


def combining_tagging(train_sents, test_sents):
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    return t2


def storing_taggers(tagger):
    from cPickle import dump
    output = open('t2.pkl', 'wb')
    dump(tagger, output, -1)
    output.close()

    from cPickle import load
    input = open('t2.pkl', 'rb')
    tagger = load(input)
    input.close()
    text = """The board's action shows what free enterprise
    is up against in our complex maze of regulatory laws ."""
    tokens = text.split()
    print tagger.tag(tokens)


def performance_limitations(tagged_corpus):
    cfd = nltk.ConditionalFreqDist(
            ((x[1], y[1], z[0]), z[1])
            for sent in tagged_corpus 
            for x, y, z in nltk.trigrams(sent))
    ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
    print 1.0 * sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N() 

if __name__ == '__main__':
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_sents = brown.sents(categories='news')
    unigram_tagger = unigram_tagging(brown_tagged_sents)
    print unigram_tagger.tag(brown_sents[2007])
    print unigram_tagger.evaluate(brown_tagged_sents)

    train_sents, test_sents = train_test(brown_tagged_sents, 0.7)
    unigram_tagger = unigram_tagging(train_sents)
    print unigram_tagger.evaluate(test_sents)

    bigram_tagger = bigram_tagging(train_sents)
    print bigram_tagger.tag(brown_sents[2007])
    print bigram_tagger.evaluate(test_sents)

    t2 = combining_tagging(train_sents, test_sents)
    t2.evaluate(test_sents)
    storing_taggers(t2)

    performance_limitations(brown_tagged_sents)
