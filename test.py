import nltk


grammar_text = open("Grammar.txt", "r").read() + open("Lexicon.txt", "r").read()
grammar = nltk.grammar.CFG.fromstring(grammar_text)
parser = nltk.parse.BottomUpChartParser(grammar)

file = open("Positive.txt", "r")
total = 0
correct = 0
for line in file:
    if line[0] == "#" or line == "\n":
        continue
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