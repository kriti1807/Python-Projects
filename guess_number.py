import random 

def guess_number(x):
    random_number=random.randint(1,x)
    guess=0
    while (guess!=random_number):
        guess=int(input("Guess a number between 1 to 10\n"))
        if (guess<random_number):
            print("Guess again. Too high")
        elif(guess<random_number):
            print("Guess again.Too low")
    print(f"Congrarulation. You guessed the number {random_number} correctly!!")
guess_number(10)