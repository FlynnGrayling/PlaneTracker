from Services import generateMap
from Services import generateHistory
import time


def setImage(flights, displayCount, darkMode):
    
    if len(flights) > 0 and displayCount < 10:
        displayHistory = False
        generateMap(flights, darkMode)
        generateHistory(flights, displayHistory)
        displayCount = displayCount + 1
    else:
        displayHistory = True
        generateHistory(flights, displayHistory)
        displayCount = 0

    print(displayCount)
    return displayCount

#800 x 480

