# affix tagger
import nltk
from nltk.corpus import brown
import sys
sys.path.append("../ch5_Categorizing_and_Tagging_Words")
from ngram_tagging import train_test


brown_tagged_sents = brown.tagged_sents(categories='news')
train_data, test_data = train_test(brown_tagged_sents, 0.7)
affix_tagger = nltk.AffixTagger(train_data)
print affix_tagger.evaluate(test_data)
