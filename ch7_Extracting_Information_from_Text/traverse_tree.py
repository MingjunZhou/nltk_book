import nltk


tree1 = nltk.Tree('NP', ['Alice'])
print tree1
tree2 = nltk.Tree('NP', ['the', 'rabbit'])
print tree2
tree3 = nltk.Tree('VP', ['chased', tree2])
tree4 = nltk.Tree('S', [tree1, tree3])
print tree4
print tree4[1]
print tree4[1].node
print tree4.leaves()
print tree4[1][1][1]
tree3.draw()

def traverse(t):
    try:
        t.node
    except AttributeError:
        print t,
    else:
        # Now we know that t.node is defined
        print '(', t.node,
        for child in t:
            traverse(child)
        print ')',

t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
traverse(t)
