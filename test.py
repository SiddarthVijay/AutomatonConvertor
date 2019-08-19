import json

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

for state in range(inputStates):
    for delta in inputDelta:
        if state not in delta:
            print(state)