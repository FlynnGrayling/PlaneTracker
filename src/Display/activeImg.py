from Services import generateMap
from Services import generateHistory
import time

#logic for displaying either map or drecent flights information
def setImage(flights, displayCount, darkMode):
    
    #if there are flights actively in bounding box display map
    if len(flights) > 0 and displayCount < 10:
        displayHistory = False
        generateMap(flights, darkMode)
        
        #call generate history to add observed flight to history list but do not display history
        generateHistory(flights, displayHistory)

        #incremenet counter to display history img after every 10 maps (10mins)
        displayCount = displayCount + 1

    #if there are no flights display info on the recently tracked flights
    else:
        displayHistory = True
        generateHistory(flights, displayHistory)
        displayCount = 0

    print(displayCount)
    return displayCount

#800 x 480

