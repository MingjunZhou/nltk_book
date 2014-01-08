from nltk.corpus import movie_reviews
import nltk
import random


def document_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


if __name__ == '__main__':
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = all_words.keys()[:2000]
    #print document_features(movie_reviews.words('pos/cv957_8737.txt'),
    #                         word_features)
    featuresets = [(document_features(d, word_features), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(5)
