import nltk
import codecs
import unicodedata


path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = codecs.open(path, encoding='latin2')
#for line in f:
#    line = line.strip()
#    print line.encode('unicode_escape')

lines = f.readlines()
line = lines[2]
print line.encode('unicode_escape')

for c in line:
    if ord(c) > 127:
        #print '%r U+%04x %s' % (c.encode('utf8'), ord(c), unicodedata.name(c))
        print '%s U+%04x %s' % (c.encode('utf8'), ord(c), unicodedata.name(c))
