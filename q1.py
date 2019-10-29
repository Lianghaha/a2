import nltk
grammar = nltk.grammar.CFG.fromstring(""" 
S -> NP VP
S -> Aux NP VP 
S -> VP
NP -> N 
NP -> DET N 
NP -> Adj N 
PP -> P NP
VP -> V Adv 
VP -> V NP Adv
VP -> V NP Adv PP

DET -> 'the' | 'their' | 'your'
Adj -> 'old' | 'red' | 'happy' 
Adv -> 'quickly' | 'slowly' 
N -> 'dogs' | 'parks' | 'statues' | 'people' 
V -> ' race' | 'walk' | 'eat' 
P -> 'in' | 'to' | 'on' | 'under ' | 'with'
Aux -> 'should' | 'will'
What -> 'what'
who -> 'who'
where -> 'where'
""")

"""
Good:
Who V DET N Adv PP
What will N V Adv PP
Where should N V DET N Adv
Should N V DET N Adv PP

Bad:
What N V Adv PP
What should N V DET N Adv PP
Where V DET N Adv PP
"""
sentence = nltk.tokenize.word_tokenize(""" Walk your dogs quickly """.lower())
parser = nltk.parse.BottomUpChartParser(grammar)
for t in parser.parse_all(sentence):
    print(t)

