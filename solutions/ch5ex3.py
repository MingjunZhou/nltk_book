import nltk


sent = "They wind back the clock, while we chase after the wind."
text = nltk.word_tokenize(sent)
print text
print nltk.pos_tag(text)
