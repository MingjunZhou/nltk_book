from nltk.corpus import gutenberg
import nltk


moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print moby.findall(r"<a> (<.*>) <man>")

# discover hypernyms
from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
print hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")
