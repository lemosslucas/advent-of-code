import numpy as np 
import re

def verify_multiplys(text):
    # expression to find the (v1, v2)
    patern = r"mul\((\d+),(\d+)\)"

    # find the subtext in format mul(v1, v2)
    multiply = re.findall(patern, text)

    # Convert the numbers in np array
    numbers = np.array([(int(v1), int(v2)) for v1, v2 in multiply])
    
    return numbers

def multiply(multiplys): 
    # multiply the only the numbers in the columns and make the sum
    return np.sum(np.prod(multiplys, axis=1))

all_multiplys = []

with open('day3.txt', 'r') as file:
    for row in file:
        multiplys = verify_multiplys(row)
        all_multiplys.extend(multiplys)

print(multiply(all_multiplys))