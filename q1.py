import nltk

grammarfile = open("q1.txt", "r")
grammartext = grammarfile.read()
grammar = nltk.grammar.CFG.fromstring(grammartext)

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

