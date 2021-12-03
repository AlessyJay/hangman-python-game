# Hang man project.
import random
from Data import words, logo, stages

randWord = random.choice(words)

# print(f'The answer is {randWord}')

print(logo)

storage = []

print(f'There are {len(randWord)} letters in a word, now let\'s guess!')

for key in range(len(randWord)):
    storage += '_'
print(storage)

isEndGame = False
lives = 7

while not isEndGame:
    askUser = input('Guess a word: ').lower()
    if askUser in storage:
        print('You\'ve guessed this letter already!')

    for position in range(len(randWord)):
        letter = randWord[position]
        if letter == askUser:
            storage[position] = letter
    print(storage)

    if '_' not in storage:
        print('You win!')
        isEndGame = True

    if askUser not in randWord:
        lives -= 1
        print(stages[lives])
        print(f'Now you have {lives} left!')
        print(f'The letter {askUser} you guess is not a part of the word!')

    if lives == 0:
        isEndGame = True
        print('You lose!')
