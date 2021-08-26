import random
# library to use
name = input("What is your name? ")
print("Good luck", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

#  function choose one random
word = random.choice(words)

print("Guess the  characters")

guesses = ''

turns =12

while turns > 0:
    # counts the number of times a user fails
    failed = 0

    # all characters from the input
    # word taking one at a time.
    for char in word:
        if char in guesses:
            print("char")

        else:
            print("_")
        # incremented in failure
        failed += 1

    if failed == 0:
    # win game if failure is 0

    print("you win")
    # print correct word
    print("the word is: ", Word)
    break


