# Building a Guessing Game (2:20:03)

secret_word = "sabueso"
guess_word = ""
tries = 1
tries_limit = 3

while secret_word != guess_word and tries <= tries_limit:
    guess_word = input("Please enter your guess: ")
    tries += 1

    if secret_word == guess_word:
        print("You win!")
    elif tries <= tries_limit:
        print("Please try again!")
    else:
        print("You lose!")