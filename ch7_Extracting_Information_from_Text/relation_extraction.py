import re
import nltk


#IN = re.compile(r'.*\bin\b(?!\b.+ing)')

IN = re.compile(r'.*\bin\b')
#print IN.search('what is in the festival spring of')
#print nltk.corpus.ieer.parsed_docs('NYT_19980315')[0].text
for i, doc in enumerate(nltk.corpus.ieer.parsed_docs('NYT_19980315')):
    #print doc.text
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                                     corpus='ieer', pattern=IN):
        print i, nltk.sem.relextract.show_raw_rtuple(rel)


from nltk.corpus import conll2002
vnv = """
(
is/V|           # 3rd sing present and
was/V|          # past forms of the verb zijn ('be')
werd/V|         # and also present
wordt/V         # past of worden ('become)
)
.*              # followed by anything
van/Prep        # followed by van ('of')
"""
VAN = re.compile(vnv, re.VERBOSE)
for doc in conll2002.chunked_sents('ned.train'):
    for r in nltk.sem.extract_rels('PER', 'ORG', doc,
                                   corpus='conll2002', pattern=VAN):
        #print nltk.sem.relextract.show_clause(r, relsym="VAN")
        print nltk.sem.relextract.show_raw_rtuple(r, lcon=True, rcon=True)

