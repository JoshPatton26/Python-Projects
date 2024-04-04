# We, Josh Patton and Vaishak Menon, declare that we have completed this
# computer code in accordance with the UAB Academic Integrity
# Code and the UAB CS Honor Code. We have read the UAB
# Academic Integrity Code and understand that any breach of the
# Code may result in severe penalties.
# Student signature(s)/initials: JP, VM
# Date: 04/03/23

import matplotlib.pyplot as plt
import numpy.random as np

def shuffleDecks(combs, start, end, type):
    split1 = list(combs[start-1:end//2])
    split2 = list(combs[(start + (end//2))-1:end-1])
        
    combinations = []
    if(type == 1):
        while(len(split1) != 0 and len(split2) != 0):
            deckChoice = np.randint(1,3)
            if(deckChoice == 1):
                combinations.append(split1.pop(0));
            elif(deckChoice == 2):
                combinations.append(split2.pop(0));
                
        if(len(split1) == 0):
            combinations.extend(split2)
        else:
            combinations.extend(split1)

    elif(type == 2):

        while(len(split1) != 0 or len(split2) != 0):
            p1 = len(split1) / len(split1 + split2)
            p2 = len(split2) / len(split1 + split2)
            val = np.choice(2, 1, p=[p1, p2])
            if(val[0] == 0):
                combinations.append(split1.pop(0))
            else:
                combinations.append(split2.pop(0))

    return combinations

def calculateCorrelations(iterations, start, end, step):

    set1 = list(range(start,end))
    if(step == 1):
        combinations = shuffleDecks(set1, start, end, step)
    elif(step == 2):
        combinations = shuffleDecks(set1, start, end, step)
        
    correlations = []
    sumi = sum(set1)
    sumsq = sum([i * i for i in set1])
    sqsum = sumi*sumi

    for j in range(iterations):
        x = 0
        for i in range(end-1):
            x += ((i+1)*combinations[i])
        y = (end-1)*x
        numerator = (y - sqsum)
        denominator = (((end-1) * sumsq) - (sqsum))
        r = numerator / denominator
        correlations.append(r)
        combinations = shuffleDecks(combinations, start, end, step)
    
    return correlations

def plotR(correlations, count):
    title = "Step " + str(count) + " Graph"
    plt.title(title)
    plt.xlabel("Run #")
    plt.ylabel("Correlation (r)")
    plt.axis([1, 15, -1, 1])
    xVal = list(range(1,16))
    plt.plot(xVal, correlations)
    plt.show()

def main():

    count = 0
    iterations = 15
    start = 1
    end = 53

    correlations = calculateCorrelations(iterations, start, end, 1)
    count += 1
    plotR(correlations, count)
    
    correlations = calculateCorrelations(iterations, start, end, 2)
    count += 1
    plotR(correlations, count)

    iterations = 15
    start = 1
    end = 105

    correlations = calculateCorrelations(iterations, start, end, 1)
    count += 1
    plotR(correlations, count)

    correlations = calculateCorrelations(iterations, start, end, 2)
    count += 1
    plotR(correlations, count)

if __name__ == "__main__":
    main() 