import nltk
from nltk.corpus import brown
from operator import itemgetter


def create_defaultdict():
    alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
    vocab = nltk.FreqDist(alice)
    v1000 = list(vocab)[:1000]
    mapping = nltk.defaultdict(lambda: 'UNK')
    for v in v1000:
        mapping[v] = v

    alice2 = [mapping[v] for v in alice]
    print alice2[:100]
    print len(set(alice2))
    
def incrementally_update():
    counts = nltk.defaultdict(int)
    for (word, tag) in brown.tagged_words(categories='news', simplify_tags=True):
        counts[tag] += 1
    print counts['N']
    print list(counts)
    aa = sorted(counts.items(), key=itemgetter(1), reverse=True)
    print aa
    print [t for t, c in aa]

def get_index():
    words = nltk.corpus.words.words('en')
    anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
    #anagrams = nltk.defaultdict(list)
    #for word in words:
    #    key = ''.join(sorted(word))
    #    anagrams[key].append(word)
    #return anagrams
    print anagrams['aeilnrt']


if __name__=='__main__':
    incrementally_update()
    get_index()
