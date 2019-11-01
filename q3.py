import nltk


def loop_over_file(file, flag):
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
    if flag:
        print("---------------------------------Positive Done ---------------------------------")
    else:
        print("--------------------------------------------------------------------------------")

    return total, correct


grammar_text = open("Grammar.txt", "r").read() + open("Lexicon.txt", "r").read()
grammar = nltk.grammar.CFG.fromstring(grammar_text)

file_Negative = open("q3 Negative.txt", "r")
file_Positive = open("q3 Positive.txt", "r")
parser = nltk.parse.BottomUpChartParser(grammar)

P_total, P_correct = loop_over_file(file_Positive, True)
N_total, N_correct = loop_over_file(file_Negative, False)
print("\nPositive: Total: {}, Correct: {}".format(P_total, P_correct))
print("\nNegative: Total: {}, Correct: {}".format(N_total, N_correct))
'''
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
'''




# TODO
# Grammar, Lexicon, Positive, Negative, Overgen, Undergen