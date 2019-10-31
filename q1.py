import nltk
grammar = nltk.grammar.CFG.fromstring(""" 
S -> NP VP
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

S -> VP
S -> Aux NP VP 

S -> who VP
S -> who Aux VP

S -> where NP VP
S -> where Aux NP VP

VPNew -> V Adv
VPNew -> V Adv PP

S -> what Aux NP VPNew

Aux -> 'should' | 'will'
what -> 'what'
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
file = open("Q3.1Negative.txt", "r")
#file = open("Q3.1Positive.txt", "r")
parser = nltk.parse.BottomUpChartParser(grammar)
for line in file:
    sentence = nltk.tokenize.word_tokenize(line)
    result = parser.parse_all(sentence)
    print("sentence: " + line.rstrip())
    print("Num of results: " + str(len(result)))
    for item in result:
        print(item)
    print("\n")

