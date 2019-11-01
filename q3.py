import nltk
grammar_file = open("q3.txt", "r")
grammar_text = grammar_file.read()
grammar = nltk.grammar.CFG.fromstring(grammar_text)

#file = open("q3 Negative.txt", "r")
file = open("q3 Positive.txt", "r")
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

print("\nTotal # sentence: {}, Correct: {}".format(total, correct))



