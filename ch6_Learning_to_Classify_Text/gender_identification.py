from nltk.corpus import names
import random
import nltk
from nltk.classify import apply_features


def gender_features(word):
    return {'last_letter': word[-1]}


if __name__ == '__main__':
    names = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(names)
    featuresets = [(gender_features(n), g) for (n, g) in names]
    # train_set, test_set = featuresets[500:], featuresets[:500]
    # LazyMap version
    train_set = apply_features(gender_features, names[500:])
    test_set = apply_features(gender_features, names[:500])
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, test_set)
    print classifier.show_most_informative_features(5)
