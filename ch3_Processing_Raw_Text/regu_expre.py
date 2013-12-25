import re, nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

print [w for w in wordlist if re.search('ed$', w)]
print [w for w in wordlist if re.search('^..j..t..$', w)]

# T9 system
print [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
