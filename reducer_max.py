#!/usr/bin/env python3

import sys

def reducer():
    maxSales = 0
    oldKey = None
    maxItem = None

    for line in sys.stdin:
        data = line.strip().split(",")
        thisKey, thisItem, thisCost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + maxItem + "," + str(maxSales))
            maxSales = 0

        # NYC, Shoes, 10.99, oldKey = None, thisKey = NYC, thisCost = 10.99, thisItem = Shoes, maxItem = Shoes
        # NYC, Books, 5.99, oldKey = NYC, thisKey = NYC, thisCost = 5.99,  = Shoes, thisItem = Books, maxItem = Shoes
        
        oldKey = thisKey
        maxSales = max(maxSales, float(thisCost))
        if maxSales == float(thisCost): # record the item with maxSales
            maxItem = thisItem
        else:
            continue
        
       
    if oldKey is not None: # for the final key
        print (oldKey + "," + maxItem + "," + str(maxSales))

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
