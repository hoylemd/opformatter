testinput = testcase.txt
testoutput = test.out
testgold = test.gold
codefiles = main.py lexer.py parser.py character.py
runcommand = python main.py

all : test

clean :
	rm -rf $(testoutput) *.pyc parsetab.py parser.out

test : clean $(testinput) $(codefiles)
	cat $(testinput) | $(runcommand) > $(testoutput)
	diff $(testoutput) $(testgold)

