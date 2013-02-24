"""
Luke Dunekacke
ECS06 hack assembler
Elements
python version 2.7
"""
from jackparser import Parser
from hackAssemblyToBinary import converter
from BadSyntaxException import BadSyntaxException
import sys


def parseFile(inputFile):
    outputFile = inputFile.split('.')[0] + ".hack"
    try:
        parse = Parser(inputFile)
        convert = converter()
        out = open(outputFile, "w")
        while parse.hasMoreCommands():
            parse.advance()
            parcedLine = parse.output().strip()
            if parcedLine != "":
                try:
                    print (parcedLine)
                    print(convert.convertStatment(parcedLine))
                    out.write(convert.convertStatment(parcedLine) + "\n")
                except BadSyntaxException:
                    print("Bad Syntax!")
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