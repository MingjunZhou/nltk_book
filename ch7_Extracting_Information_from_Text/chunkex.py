import nltk


def find_chunks(tagged_sents, regexp_rule):
    cp = nltk.RegexpParser(regexp_rule)
    for sent in tagged_sents:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'CHUNK': print subtree


sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
            ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
