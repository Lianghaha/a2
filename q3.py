import nltk
grammar = nltk.grammar.CFG.fromstring(""" 
S -> NP VP
S -> Name VP
NP -> N
NP -> NPro
NP -> Det NP
NP -> NP PP
NP -> Adj N
Adj -> Adj Adj
VP -> V Adv
VP -> Adv V
VP -> V
PP -> P NP
 

Name -> 'Nadia'
NPro -> 'she' | 'her'
N -> 'cat' | 'fur'  
V -> 'left' | 'ate' | 'arrived'
Adv -> 'immediately' | 'slowly'
Det -> 'the'
P -> 'with'
Adj -> 'long' | 'soft' | 'tall'

""")
#nltk.app.srparser()

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



