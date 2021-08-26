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
    for char in word:        # comparing that character with # the character in guesses

