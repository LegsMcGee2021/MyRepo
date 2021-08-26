import random


def randomize():
    number = random.randint(1, 100)
    global number


def start():
    while True:
        try:
            guess = int(input("Welcome to the random number game, what is your first guess?\n"))
            if guess > 100:
                print("You know that's to high\n")
                continue
            elif guess < 1:
                print("You know that's to low\n")
                continue
            else:
                break
        except ValueError:
            print("I'm sorry, that wasn't a number, please try again\n")
            continue

    if guess == number:
        print("How in the ****, you got that on the first try, good job\n")
        replay()
    else:
        if guess < number:
            print("To low\n")
            remaining_guesses()
        elif guess > number:
            print("To high\n")
            remaining_guesses()


def remaining_guesses():
    guesses = 2
    while guesses < 6:
        while True:
            try:
                guess = int(input("You're on guess " + str(guesses) + ", what is your next guess?\n"))
                if guess > 100:
                    print("You know that's to high\n")
                    continue
                elif guess < 1:
                    print("You know that's to low\n")
                    continue
                else:
                    break
            except ValueError:
                print("I'm sorry, that wasn't a number, please try again\n")
                continue

        if guess == number:
            print("Good job, you got the number\n")
            break
        else:
            if guess > number:
                print("To high\n")
                guesses += 1
            elif guess < number:
                print("To low\n")
                guesses += 1
    if guesses == 6:
        print("Oh no, you ran out of guesses\n")
    replay()


def replay():
    re = input("Would you like to play again?\n")
    if re == "y" or re == "Y" or re == "yes" or re == "Yes":
        randomize()
        start()
    else:
        print("Have a great day")


start()
