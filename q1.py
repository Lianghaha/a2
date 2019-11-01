import nltk

grammar_text = open("q1.txt", "r").read()
grammar = nltk.grammar.CFG.fromstring(grammar_text)

#file = open("q1 Negative.txt", "r")
file = open("q1 Positive.txt", "r")
parser = nltk.parse.BottomUpChartParser(grammar)

total = 0
correct = 0

for line in file:
    print("")
    sentence = nltk.tokenize.word_tokenize(line)
    result = parser.parse_all(sentence)
    total += 1
    if len(result) > 0:
        correct += 1
    print("sentence: " + line.rstrip())
    print("Num of results: " + str(len(result)))
    for item in result:
        print(item)

print("\nTotal: {}, Correct: {}".format(total, correct))

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
