import nltk


def loop_over_file(file, positive, prof, overgen):
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

    if positive == 1 and prof == 1:
        print("---------------------------------Prof Positive Done ---------------------------------")
    if positive == 1 and prof == 0:
        print("---------------------------------Positive Done --------------------------------------")
    if positive == 0 and prof == 1:
        print("---------------------------------Prof Negative Done ---------------------------------")
    if positive == 0 and prof == 0:
        print("---------------------------------Negative Done --------------------------------------")
    if overgen == 1:
        print("---------------------------------Overgen Done ---------------------------------------")
    if overgen == 0:
        print("---------------------------------Undergen Done --------------------------------------")

    return total, correct


grammar_text = open("Grammar.txt", "r").read() + open("Lexicon.txt", "r").read()
open("temp/allgrammar.txt", "w").write(grammar_text)
grammar = nltk.grammar.CFG.fromstring(grammar_text)

prof_Negative = open("q3 Negative.txt", "r")
prof_Positive = open("q3 Positive.txt", "r")
Negative = open("Negative.txt", "r")
Positive = open("Positive.txt", "r")
Overgen = open("Overgen.txt", "r")
Undergen = open("Undergen.txt", "r")
parser = nltk.parse.BottomUpChartParser(grammar)

P_prof_total, P_prof_correct = loop_over_file(prof_Positive, 1, 1, 2)
P_total, P_correct = loop_over_file(Positive, 1, 0, 2)
N_prof_total, N_prof_correct = loop_over_file(prof_Negative, 0, 1, 2)
N_total, N_correct = loop_over_file(Negative, 0, 0, 2)
Over_total, Over_correct = loop_over_file(Overgen, 2, 2, 1)
Under_total, Under_correct = loop_over_file(Undergen, 2, 2, 0)
print("\n(Prof)Positive: Total: {}, Correct: {}".format(P_prof_total, P_prof_correct))
print("\nPositive: Total: {}, Correct: {}".format(P_total, P_correct))
print("\n(Prof)Negative: Total: {}, Correct: {}".format(N_prof_total, N_prof_correct))
print("\nNegative: Total: {}, Correct: {}".format(N_total, N_correct))
print("\nOvergen: Total: {}, Correct: {}".format(Over_total, Over_correct))
print("\nUndergen: Total: {}, Correct: {}".format(Under_total, Under_correct))
