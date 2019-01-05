import random

# Constants to be used in the implementation
WORD_LIST = [
    "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
    "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'


def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)


# Main program starts here
random_seed()


def choose_word(word_list):
    return random.choice(word_list)


def find_letter(guess, word):
    nums = []
    for num, letter in enumerate(word):
        if letter == guess:
            nums.append(num)
    return nums


def change_letter(nums, guess, guessed_word):
    for x in nums:
        guessed_word[x] = guess
    return guessed_word


def end_game(word):
    print("You lost! The secret word was {}".format(word))
    quit()


def main():
    word = choose_word(WORD_LIST)
    print("The word you need to guess has {} characters".format(len(word)))
    game = True
    guessed_letters = []
    guessed_word = list(len(word) * CHAR_PLACEHOLDER)
    guesses = 1
    while game:
        if guesses == 13:
            end_game(word)
        print("You are on guess {}/12".format(guesses))
        print("Word to guess: {}".format(" ".join(str(x) for x in guessed_word)))
        guess = input("Choose a letter: ")
        if guess not in guessed_letters:
            if guess in word:
                print("You guessed correctly!")
                nums = find_letter(guess, word)
                guessed_word = change_letter(nums, guess, guessed_word)
                if guessed_word == list(word):
                    print("You win!")
                    print("Word to guess: {}".format(" ".join(str(x) for x in guessed_word)))
                    quit()
            else:
                print("The letter is not in the word!")
            guesses += 1
        else:
            print("You have already guessed that letter!")
        guessed_letters.append(guess)



main()