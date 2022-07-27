# Python Coin Flip Simulator

import random

# Totals
num_heads = 0
num_tails = 0

n = 1
while n <= 10:
    # Flip a Coin
    randNum = random.randrange(1, 3)
    if randNum == 1:
        num_heads += 1
        print("Heads")
    else:
        num_tails += 1
        print("Tails")

    # Increment n
    n += 1

print("Goodbye")


# Use a for loop to run a set # of times
for n in range(8):
    print("hi")
