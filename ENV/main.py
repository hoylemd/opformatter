# coding: utf-8
from lexer import Lexer
from parser import Parser
from preprocessor import InputBlock
import fileinput

if __name__ == "__main__":
    lines = []

    for line in fileinput.input():
        lines.append(line)

    input = InputBlock("".join(lines));

    f = open ("tokens.txt", "w")
    f.write(Lexer().readTokens(input.raw))
    f.close();

    parser = Parser(Lexer())

    parser.parse(input.raw)

    if parser.error <> True:
        print parser.character.output()
