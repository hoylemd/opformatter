# coding: utf-8
from lexer import Lexer
from parser import Parser
import fileinput

if __name__ == "__main__":
    lines = []

    for line in fileinput.input():
        lines.append(line)

    input_string = "".join(lines)

    f = open ("tokens.txt", "w")
    f.write(Lexer().readTokens(input_string))
    f.close();

    parser = Parser(Lexer())

    parser.parse(input_string)

    if parser.error <> True:
	print parser.character.output()
