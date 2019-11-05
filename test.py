import nltk
grammar_text = open("Grammar.txt", "r").read() + open("Lexicon.txt", "r").read()
grammar = nltk.grammar.CFG.fromstring(grammar_text)

sentence = nltk.tokenize.word_tokenize(""" she want """)
parser = nltk.parse.BottomUpChartParser(grammar)
for t in parser.parse_all(sentence):
    print(t)