testinput = testcase.txt
testoutput = test.out
testgold = test.gold
prefix = obsidianFormat
codefiles = main.py $(prefix)_lex.py $(prefix)_yacc.py $(prefix)_character.py
runcommand = python main.py

all : test

test : $(testinput) $(codefiles)
	cat $(testinput) | $(runcommand) > $(testoutput)
	diff $(testoutput) $(testgold)

clean :
	rm -rf $(testoutput) *.pyc parsetab.py parser.out
