"""
Luke Dunekacke
ECS06 hack assembler
Elements
python version 2.7
"""
from jackparser import Parser
import sys


def parseFile(inputFile):
    outputFile = inputFile.split('.')[0] + ".hack"
    try:
        parse = Parser(inputFile)
        out = open(outputFile, "w")
        while parse.hasMoreCommands():
            parse.advance()
            out.write(parse.output().strip() + "\n")
        out.close()
    except IOError:
        print("File " + inputFile +" can not be open")
        


def main():
    if len(sys.argv) < 2:
        print ("No file name given")
    else:
        parseFile(sys.argv[1])


if __name__ == '__main__':
    main()