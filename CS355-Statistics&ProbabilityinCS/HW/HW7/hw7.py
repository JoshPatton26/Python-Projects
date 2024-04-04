import numpy.random as rand
import matplotlib.pyplot as plot

def main():
    x = []
    y = 15
    count = 1000

    while (count != 0):
        wait = rand.randint(10, 30)

        if (wait < y):
            x.append(y - wait)
        else:
            x.append((y*2) - wait)
        
        count = count - 1
        
    plot.hist(x, bins=8)
    plot.title("Problem 1")
    plot.xlabel("Wait time (min)")
    plot.ylabel("Frequency")
    plot.xlim(0,16)
    plot.show()

    return 0

if __name__ == "__main__":
    main()