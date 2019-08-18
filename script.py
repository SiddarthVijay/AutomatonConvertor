# Library imports
import json

# Custom function imports
from helper import *

# Reading and processing inputs
inputFile = open(r"input.json", "r")
jsonObject = inputFile.read()
parsedJSON = json.loads(jsonObject)

# Output objects


# Find all states one by one


# Outputing the answer in JSON
outputFile = open(r"output.json", 'w')
dfaJSON = json.dumps(dfaDesc)
print(dfaJSON, file=outputFile)