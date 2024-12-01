import numpy as np

X = []
Y = []

# read the file
with open("day1.txt", "r") as file:
    for row in file:
        x, y = row.split()
        X.append(int(x))
        Y.append(int(y))    

X = np.array(X)
Y = np.array(Y)

# order the arrays
x_sort = np.sort(X)
y_sort = np.sort(Y)

frequencies = []
for x in x_sort:
    frequencie = 0
    for y in y_sort:
        if x == y:
            frequencie += 1 
    frequencies.append(frequencie)

apparitions = np.array(frequencies)

# multiply the similarity
similarity = np.multiply(x_sort, frequencies)

# find the total similarity
total_similarity = np.sum(similarity)

print(total_similarity)