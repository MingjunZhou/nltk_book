import feedparser, nltk
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
post = llog.entries[2]
print post.title
content = post.content[0].value
print content[:70]
print nltk.word_tokenize(nltk.clean_html(llog.entries[2].content[0].value)) 
