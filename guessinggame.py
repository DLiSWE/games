import random

highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number from 1 and {}".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Congrats {} was the answer!".format(guess))
        break
    else:
        if guess < answer:
            print("No, {} is less than the answer. Please try again.".format(guess))
        else:
            print("No, {} is higher than the answer. Try again".format(guess))