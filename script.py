# Library imports
import json

# Custom function imports
from helper import phiEntry, multiStates

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
outputStates = inputStates
outputAlphabet = inputAlphabet
outputStart = inputStart
outputFinal = []
outputDelta = []

# Find all states one by one
for state in range(inputStates):
    for delta in inputDelta:
        if state in delta:
            # print(state, delta)
            for alphabet in inputAlphabet:
                if alphabet in delta:
                    currentFinalStates = delta[-1]
                    if len(currentFinalStates) == 1:
                        outputDelta.append(delta)
                    else:
                        outputStates += 1
                        multiOutputs()

# Outputing the answer in JSON
# outputFile = open(r"output.json", 'w')
# dfaJSON = json.dumps(dfaDesc)
# print(dfaJSON, file=outputFile)