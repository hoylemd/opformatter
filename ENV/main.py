# coding: utf-8
import sys
from lexer import Lexer
from parser import Parser
from preprocessor import InputBlock
import fileinput

if __name__ == "__main__":
    lines = []

    # read the input file
    for line in fileinput.input():
        lines.append(line)

    # preprocess the text
    input = InputBlock("".join(lines))

    # start the character
    character = input.spawnCharacter()

    # lex the text
    f = open ("tokens.txt", "w")
    f.write(Lexer().readTokens(input.parsable))
    f.close();

    # parse the text
    parser = Parser(Lexer(), character)
    parser.parse(input.parsable)

    # if the parse proceeded reasonably, add the preprocessed blocks
    if parser.error <> True:
        print parser.character.output()
