from Services import generateMap
from Services import generateHistory
import time

def setImage(flights):
    while True:
        generateMap(flights)

        generateHistory(flights)

        time.sleep(60)