from nltk.corpus import brown
import nltk


def nouns():
    brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
    word_tag_pairs = nltk.bigrams(brown_news_tagged)
    print list(nltk.FreqDist(a[1] for a, b in word_tag_pairs if b[1] == 'N'))

def verbs():
    wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
    # word_tag_fd = nltk.FreqDist(wsj)
    # print [word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')]
    cfd1 = nltk.ConditionalFreqDist(wsj)
    print cfd1['yield'].keys()
    print cfd1['cut'].keys()
    print [w for w in cfd1.conditions() if 'VD' in cfd1[w] and 'VN' in cfd1[w]]
    idx1 = wsj.index(('kicked', 'VD'))
    print wsj[idx1-4:idx1+1]
    idx2 = wsj.index(('kicked', 'VN'))
    print wsj[idx2-4:idx2+1]

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

def process(sentence):
    for (w1, t1), (w2, t2), (w3, t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')) :
            print w1, w2, w3


if __name__ == "__main__":
    tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
    for tag in sorted(tagdict):
        print tag, tagdict[tag]
    for tagged_sent in brown.tagged_sents():
        process(tagged_sent)
