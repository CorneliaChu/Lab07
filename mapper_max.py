#!/usr/bin/env python3

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",")
        count = 0
        for i in data:
            count += 1
        if count < 4:
            continue
        if count > 4:
            data = data[0:4]
        timestamp, city, item, cost = data
        print(city + "," + item + "," + cost)

if __name__ == "__main__":
    # what function should run when python mapper.py is called?
    mapper()
