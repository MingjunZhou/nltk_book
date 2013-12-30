import nltk
from nltk.corpus import brown
import collections


brown_tagged_words = brown.tagged_words()
#brown_cfd = nltk.ConditionalFreqDist((tag, word) for word, tag in brown_tagged_words)
#brown_cfd = nltk.ConditionalFreqDist(brown_tagged_words)
#print brown_cfd.conditions()
#print len(brown_cfd.conditions())
#print brown_cfd.keys()
#print len(brown_cfd.values())
#print len(brown_cfd.keys())
#print brown_cfd['NN']
stat = collections.defaultdict(set)
for word, tag in brown_tagged_words:
    stat[word].add(tag)

stat2 = {}
for key in stat.keys():
    stat2[key] = len(stat[key])

stat3 = collections.defaultdict(int)
stat4 = collections.defaultdict(set)
for key in stat2.keys():
    stat3[stat2[key]] += 1
    stat4[stat2[key]].add(key)

max_tags = max(stat2.values())
for i in range(1, max_tags+1):
    print "%d     %d" %(i, stat3[i])

brown_sents = brown.sents()
for item in stat4[max_tags]:
    flag = 0
    tagset = set()
    sent_idx = -1
    tagf = {}
    for sent in brown.tagged_sents():
        if len(tagset) < max_tags:
            sent_idx += 1
            for word, tag in sent:
                if (word == item and tag not in tagset):
                    tagset.add(tag)
                    tagf[tag] = sent_idx
    for key in tagf:
        print key + ": " + ' '.join(brown_sents[tagf[key]])
