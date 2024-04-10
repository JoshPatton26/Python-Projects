import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generateProblem():
    left = random.randrange(MIN_OPERAND, MAX_OPERAND)
    right = random.randrange(MIN_OPERAND, MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start")
print("--------------------")

start = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generateProblem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end = time.time()
totalTime = end - start
print("--------------------")
print("Nice Work! You answered all the questions in {} seconds!".format(totalTime))
print("You had {} wrong asnwers.".format(wrong))