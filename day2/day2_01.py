import numpy as np 

def verifiy_security(vetor):
    # determine if was a increasing or decreasing reports
    first_diff = vetor[0] - vetor[1]
    
    for i in range(len(vetor)):
        if i != len(vetor) - 1:
            # verifiy if the number increasing or decreasing
            diff = vetor[i] - vetor[i + 1]
            if (first_diff > 0 and diff < 0) or (first_diff < 0 and diff > 0):
                return False
            
            # verifify if the diff is beetwen 1 to 3
            if np.abs(diff) > 3 or np.abs(diff) < 1:
                return False
            
    return True

safe = 0
with open('day2.txt', 'r') as file:
    for row in file:
        elements = list(map(int, row.split()))
        if verifiy_security(np.array(elements)):
            safe += 1

print(safe)
