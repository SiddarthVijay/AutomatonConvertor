# Library imports
import json

# Custom function imports
from helper import *

# Reading and processing inputs
inputFile = open(r"input.json", "r")
jsonObject = inputFile.read()
parsedJSON = json.loads(jsonObject)

# Input objects
inputStates = parsedJSON["states"]
inputAlphabet = parsedJSON["letters"]
inputStart = parsedJSON["start"]
inputFinal = parsedJSON["final"]
inputDelta = parsedJSON["t_func"]

# Output objects
outputStates = parsedJSON["states"]
outputAlphabet = parsedJSON["letters"]
outputStart = parsedJSON["start"]
outputFinal = parsedJSON["final"]
outputDelta = parsedJSON["t_func"]

# Find all states one by one


# Outputing the answer in JSON
# outputFile = open(r"output.json", 'w')
# dfaJSON = json.dumps(dfaDesc)
# print(dfaJSON, file=outputFile)