def multiOutputStates(inputAlphabet, delta, inputDelta, outputDelta):
    currentFinalStates = delta[-1]
    newSmallFinalStates = []
    # The old final state will be my new input state
    for alphabet in inputAlphabet:
        singleDeltaEntry = []
        singleDeltaEntry.append(currentFinalStates)
        singleDeltaEntry.append(alphabet)
        newSmallFinalStates = []
        if type(currentFinalStates) != int:
            for newSmallInputState in currentFinalStates:
                for processingDelta in inputDelta:
                    if newSmallInputState in processingDelta:
                        if alphabet in processingDelta:
                            newSmallFinalStates.append(processingDelta[-1][0])
            singleDeltaEntry.append(newSmallFinalStates)
            outputDelta.append(singleDeltaEntry)

            if len(newSmallFinalStates) > 1:
                print(newSmallFinalStates)
            else:
                # return 0, 0
                print()
        else:
            singleDeltaEntry.append(currentFinalStates)
            outputDelta.append(singleDeltaEntry)
            return 0, 0


def phiEntry(state, delta, outputStates):
    return