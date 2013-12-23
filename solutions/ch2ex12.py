import sys
sys.path.append("..")
from utils.text_proc import words_yield

f = open('../data/pride and prejudice.txt', 'r')
newf = open('new pride and prejudice.txt', 'wb')
words = words_yield(f)
i = 0
for word in words:
    i = (i + 1) % 3
    if i % 3 == 0:
        newf.write('like ')
    newf.write(word + ' ')
f.close()
newf.close()
