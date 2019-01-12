"""
Probabilty Simulation by Alex Funnell. Written in Python 3.7.2. 

||| DESCRIPTION |||

Probabilty Simulation is a python program to calculate expirmental probability. 
It can be configured heavily to your needs. You can change the values 
in the "VARIABLES" section below, but the main calculations are not to be touched 
in order to work successfully everytime. It will display a table at t

What each value does:


probabilitysimulation is updated for bugfixes and changes to the GitHub page here: https://github.com/C74C3/probabilitysimulation 

Thank you for downloading. You can explore more at https://cyber.c7division.com
"""

import random
from timeit import default_timer as timer

# VARIABLES

coinFlip = "true"
diceRoll = "false"
mincount = 1
maxcount = 6
times = 100000

# NO TOUCHEY BELOW HERE :)

count = 0
oneCount = 0
twoCount = 0
threeCount = 0
fourCount = 0
fiveCount = 0
sixCount = 0
headsCount = 0
tailsCount = 0
flipTimes = times

if diceRoll == "true":
    start = timer()
    while count < times:
        rollnum = random.randint(mincount, maxcount)

        if rollnum == 1:
            oneCount = oneCount + 1

        elif rollnum == 2:
            twoCount = twoCount + 1

        elif rollnum == 3:
            threeCount = threeCount + 1
            
        elif rollnum == 4:
            fourCount = fourCount + 1

        elif rollnum == 5:
            fiveCount = fiveCount + 1
        
        elif rollnum == 6:
            sixCount = sixCount + 1

        count = count + 1
        print(str(count) + "/" + str(times))

        print("Number of 1s rolled: " + str(oneCount))
        print("Number of 2s rolled: " + str(twoCount))
        print("Number of 3s rolled: " + str(threeCount))
        print("Number of 4s rolled: " + str(fourCount))
        print("Number of 5s rolled: " + str(fiveCount))
        print("Number of 6s rolled: " + str(sixCount))
        end = timer()

elif coinFlip == "true":
    start = timer()
    while count < flipTimes:
        flipnum = random.randint(1,2)

        if flipnum == 1:
            headsCount = headsCount + 1

        elif flipnum == 2:
            tailsCount = tailsCount + 1

        count = count + 1
        print(str(count) + "/" + str(flipTimes))

    print("Number of heads: " + str(headsCount))
    print("Number of tails: " + str(tailsCount))
    end = timer()
    total = headsCount + tailsCount
    print("Total: " + str(total))
    totalTime = end - start
    totalTime = round(totalTime, 3)
    print("Time elapsed: " + str(totalTime) + " seconds.")
