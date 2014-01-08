from nltk.corpus import names
import nltk
import random


def gender_features2(name):
    features = {}
    features["firstletter"] = name[0].lower()
    features["lastletter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features


def gender_features(word):
    return {'last_letter': word[-1]}


if __name__ == '__main__':
    names = ([(name, 'male') for name in names.words('male.txt')] +
             [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(names)
    # development sets
    train_names = names[1500:]
    devtest_names = names[500:1500]
    test_names = names[:500]

    train_set = [(gender_features(n), g ) for (n, g) in train_names]
    devtest_set = [(gender_features(n), g) for (n, g) in devtest_names]
    test_set = [(gender_features(n), g) for (n, g) in test_names]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print nltk.classify.accuracy(classifier, devtest_set)
