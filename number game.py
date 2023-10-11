import random

def guess_number():
    num= random.randint(1, 100)

    print("Welcome to the Number Guessing Game!!!")
    print("I am thinking of a number between 1 to 100.\n")

    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number:\t"))
            attempts += 1

            if guess< num:
                print("The guessed number is lower than the secret number\n")
            elif guess> num:
                print("The guessed number is greater than the secret number\n")
            else:
                print(f"Congratulations!!! You guessed the secret number {num}\n")
                break
            print(f"Number of attempts you have are {max_attempts - attempts}\n")
        except ValueError:
            print("Please Enter a Valid Number.\n")
    if attempts == 3:
        print("Sorry, You have reached the maximum number of attempts.\n")
        print(f"---\tThe secret number is {num}\t---")

guess_number()
