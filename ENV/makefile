testinput = testcase.txt
testoutput = test.out
testgold = test.gold
charactergold = character_blank.gold
codefiles = main.py tokens.py lexer.py parser.py character.py
runcommand = python main.py

all : test

clean :
	rm -rf $(testoutput) *.pyc parsetab.py parser.out tokens.txt

test : clean $(testinput) $(codefiles)
	cat $(testinput) | $(runcommand) > $(testoutput)
	diff $(testoutput) $(testgold)

test_character : clean $(codefiles)
	python test_character.py > $(testoutput)
	diff $(testoutput) $(charactergold) > .output

