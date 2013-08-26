from obsidianFormat_lex import Lexer
from obsidianFormat_yacc import Parser
import fileinput

if __name__ == "__main__":
    lines = []

    for line in fileinput.input():
        lines.append(line)

    input_string = "".join(lines)

    lexer = Lexer()
    parser = Parser(Lexer())

    parser.parse(input_string)

    if parser.error <> True:
	print parser.character.output()
