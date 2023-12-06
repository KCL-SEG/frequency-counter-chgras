"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        currentItem = str(item)
        if currentItem in frequencies:
            frequencies[currentItem] = frequencies[currentItem] + 1
        else:
            frequencies[currentItem] = 1

    return frequencies