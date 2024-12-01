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

# do the dif a each position
dist = np.abs(x_sort - y_sort)

# find the total dist
total_dist = np.sum(dist)

print(total_dist)