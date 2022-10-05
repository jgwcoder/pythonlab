# Part 1
word = "Lights"

# Part 2
print("Welcome to the Word Guesser!")
print("The player has 10 tries to guess the word correctly.")
answer = input("Are you ready to start? [Yes/No]")

if answer == "Yes":
    print("The game has started.")
elif answer == "No":
    print("The game has ended")
else:
    print("Invalid answer")
    exit()

# Part 3
fails = 0

# Part 4
storage = []

while fails < 10:
    for char in word:
        print('_',end='')

    print('')
    
    guess = input("Guess the word: ")
    storage += guess
    # Part 5
    if guess == word:
        print("Correct!")
        exit()
    else:
        print("That is incorrect.")
        fails += 1

    #Part 6
    guessed_word = ''

    for char in word:
        if char in storage:
            print(char, end='')
            guessed_word += char
        else:
            print('_', end='')
            guessed_word += '_'
        
    print('')

    #Part 6.5
    if guessed_word == word:
        print("Congrats, you win!")
        exit()