import nltk


text = nltk.word_tokenize("And now for something completely different")
print nltk.pos_tag(text)

# check the doc for the tag
print nltk.help.upenn_tagset('RB')
#print nltk.help.upenn_brown_tagset('NN.*')
print nltk.corpus.brown.readme()

# homonyms
text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print nltk.pos_tag(text)


# text.similar
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print text.similar('woman')
# print text.similar('bought')
# print text.similar('over')
# print text.similar('the')

sent = '''
The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN of/IN both/ABX governments/NNS ''/'' ./.
'''

print [nltk.tag.str2tuple(t) for t in sent.split()]
