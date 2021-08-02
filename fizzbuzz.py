def fizz_buzz(number: int) -> str:
    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return int(number)


input("Play Fizz Buzz. Press Enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = int(input("Your turn: "))

    if players_answer != correct_answer:
        print("You lose, the right answer was {}.".format(correct_answer))
        break
else:
    print("You got it. {} was the answer".format(correct_answer))

"""
Take turns with bot. 
"""