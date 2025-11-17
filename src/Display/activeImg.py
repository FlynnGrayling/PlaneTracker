from Services import generateMap
from Services import generateHistory
import time


def setImage(flights, displayCount):
    
    if len(flights) > 0 and displayCount < 10:
        generateMap(flights)
        generateHistory(flights)
        displayCount = displayCount + 1
    else:
        generateHistory(flights)
        displayCount = 0

    print(displayCount)
    return displayCount

