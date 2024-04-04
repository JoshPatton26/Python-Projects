import random


def factorial(x):
    if(x == 0):
        return 1
    else:
        return x * factorial(x-1)

print("===========================================================")
        
ctok = factorial(13) / (factorial(1)*(factorial(13-1)))
print('# choices for type of 3 matching cards = ', int(ctok))

tok = factorial(4) / (factorial(3)*(factorial(4-3)))
print('\nPossibilities for 3 matching cards = ', int(tok))

cpair = (factorial(12) / (factorial(1)*(factorial(12-1))))
print('\n# choices for type of matching pair = ', int(cpair))

pair = (factorial(4) / (factorial(2)*(factorial(4-2))))
print('\nPossibilities for a matching pair = ', int(pair))

fch = factorial(52) / (factorial(5)*factorial(52-5))

p = (ctok * tok * cpair * pair) / fch
print("\nProbability to get a full house drawn at random = %.4f" %p)

print("===========================================================")

spade = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
diamond = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
club = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
hearts = ["2","3","4","5","6","7","8","9","J","Q","K","A"]
hand = []

j = 1
fhc = 0
r = 1000
for j in range(r):
    for i in range(5):
        n = random.randrange(1,4)
        if(n == 1):
            hand.append(random.choice(spade))
        elif(n == 2):
            hand.append(random.choice(club))
        elif(n == 3):
            hand.append(random.choice(hearts))
        else:
            hand.append(random.choice(diamond))

    print("\n", hand)
    s = set(hand)

    if(len(s) == 2):
        print("Full House!!")
        fhc = fhc + 1

    hand = []

if(fhc > 1):
    print("You got %d full houses " %fhc, "out of %d attempts"  %r)

print(fhc / r)