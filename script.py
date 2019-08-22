# Library imports
import json

# Custom function imports
from helper import multiOutputStates, phiEntry

# Reading and processing inputs
inputFile = open(r"input2.json", "r")
jsonObject = inputFile.read()

inputFile.close()

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

# Required variables
processedStates = []

# Find all states one by one
for state in range(inputStates):
    if state not in processedStates:
        for delta in inputDelta:
            if state in delta:
                for alphabet in inputAlphabet:
                    if alphabet in delta:
                        currentFinalStates = delta[-1]
                        if len(currentFinalStates) == 1:
                            outputDelta.append(delta)
                        else:
                            outputStates += 1
                            outputDelta.append(delta)
                            isThereMore = multiOutputStates(inputAlphabet, delta, inputDelta, outputDelta)
                            if isThereMore[0] == 1:
                                multiOutputStates(inputAlphabet, isThereMore[1], inputDelta, outputDelta)

# Outputing the answer in JSON
# outputFile = open(r"output.json", 'w')
# dfaJSON = json.dumps(dfaDesc)
# print(dfaJSON, file=outputFile)

# outputFile.close()
print(outputDelta)