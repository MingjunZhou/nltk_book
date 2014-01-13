import nltk


grammar = r"""
NP: {<DT|JJ|NN.*>+}             # Chunk sequences of DT, JJ, NN
PP: {<IN><NP>}                  # Chunk prepositions followed by NP
VP: {<VB.*><NP|PP|CLAUSE>+$}    # Chunk verbs and their arguments
CLAUSE: {<NP><VP>}              # Chunk NP, VP
"""

cp = nltk.RegexpParser(grammar)
sentence1 = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
            ("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print cp.parse(sentence1)

sentence2 = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
             ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
             ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print cp.parse(sentence2)

cp = nltk.RegexpParser(grammar, loop=2)
print cp.parse(sentence2)
