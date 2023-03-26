#number game App
import random

#generate a number between [1 .. 10]
secret_number = random.randint(1,10)

while True:
    guess = int(input("guess a number between [1 .. 10]:\n"))
    
    if(guess == secret_number):
        print("Good job! my number was {}".format(secret_number))
        break

    else: 
        print("that \'s not it")
        continue