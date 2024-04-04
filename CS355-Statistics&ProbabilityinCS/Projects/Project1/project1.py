import matplotlib.pyplot as plt

def splitArray(combs, start, end, type):
    split1 = combs[start-1:end//2]
    split2 = combs[(start + (end//2))-1:end-1]

    combinations = []
    if(type == 1):
        for i in range(end//2):
            combinations.append(split1[i])
            combinations.append(split2[i])
    elif(type == 2):
        for i in range(end//2):
            combinations.append(split2[i])
            combinations.append(split1[i])
    return combinations

def shuffle(iterations, start, end, step):

    set1 = list(range(start,end))
    if(step == 1):
        combinations = splitArray(set1, start, end, step)
    elif(step == 2):
        combinations = splitArray(set1, start, end, step)
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
        combinations = splitArray(combinations, start, end, step)
    
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

    correlations = shuffle(iterations, start, end, 1)
    count += 1
    plotR(correlations, count)
    
    correlations = shuffle(iterations, start, end, 2)
    count += 1
    plotR(correlations, count)

    iterations = 15
    start = 1
    end = 105

    correlations = shuffle(iterations, start, end, 1)
    count += 1
    plotR(correlations, count)

    correlations = shuffle(iterations, start, end, 2)
    count += 1
    plotR(correlations, count)

if __name__ == "__main__":
    main() 