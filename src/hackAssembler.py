"""
Luke Dunekacke
ECS06 hack assembler
Elements
python version 2.7
"""
from jackparser import Parser
import sys


def parseFile(inputFile, outputFile):
    out = open(outputFile, "w")
    c = Parser(inputFile)
    while c.hasMoreCommands():
        c.advance()
        out.write(c.output().strip() + "\n")
    out.close()


def main():
    if len(sys.argv) < 2:
        print ("No file name given")
    else:
        parseFile(sys.argv[1], "out.hack")


if __name__ == '__main__':
    main()