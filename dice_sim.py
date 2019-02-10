# Python Script for Dice Simulator: Intentionally re-invent
# Author: Vignesh Narasimhulu

import time

#get current time
now=str(time.time())

#get last element
lucky=now[-1]

#Function: returns 
def dice(x):
    #convert input to string, for comparison
    y=str(x)

    #compare input with lucky number
    if (y == lucky):
        #print (str(x) +":"+ str(lucky))
        #if match found, exit with non-zero
        return x
    else:
        #print (str(x) +";"+ str(lucky))
        #if match not found, exit with zero
        return 0

for i in range(1,7):
    roll=dice(i)
    #match-found: print number and exit
    if(roll):
        print (i)
        break

#If no match found, print number 6       
if(not roll):
    print ("6")
