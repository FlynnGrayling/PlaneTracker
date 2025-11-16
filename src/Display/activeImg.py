from Services import generateMap
from Services import generateHistory
import time


def setImage(flights):
    storedFlights = flights 
    

    if(storedFlights == flights):
        generateMap(flights)

        generateHistory(flights)

