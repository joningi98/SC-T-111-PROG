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


def change_letter(nums, correct_guess, guess):
    for x in nums:
        correct_guess[x] = guess
    return correct_guess


def end_game(correct_guess):
    print("You won!")
    print("Word to guess: {}".format(" ".join(str(x) for x in correct_guess), end=''))


def main():
    chosen_word = choose_word(WORD_LIST)
    print("The word you need to guess has {} characters".format(len(chosen_word)))
    guesses = 0
    correct_guess = list(len(chosen_word) * CHAR_PLACEHOLDER)
    guessed_letters = []
    game = True
    while game:
        if guesses == MAX_GUESS:
            print("Word to guess: {}".format(" ".join(str(x) for x in correct_guess), end=''))
            print("You lost! The secret word was {}".format(chosen_word))
            quit()

        print("Word to guess: {}".format(" ".join(str(x) for x in correct_guess), end=''))
        guess = input("Choose a letter: ")
        if guess not in guessed_letters:
            if guess in chosen_word:
                nums = find_letter(guess, chosen_word)
                correct_guess = change_letter(nums, correct_guess, guess)
                print("You guessed correctly!")
                if correct_guess == list(chosen_word):
                    end_game(correct_guess)
                    quit()

            else:
                print("The letter is not in the word!")
            guessed_letters.append(guess)
            guesses += 1
        else:
            print("You have already guessed that letter!")
            pass
        print("You are on guess {}/12".format(guesses))


main()
