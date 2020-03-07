from create_word_list import create_word_list
import random


class Hangman:
    def __init__(self):
        self.word = list()
        self.guesses = 0
        self.lives = 8
        self.progress = list()
        self.used_chars = list()

    def generate_word(self):    # chooses a word based on a wordlist created from "create_word_list.py"
        words = create_word_list('words.txt', 20)
        self.word = list(random.choice(words).upper())

    def starting_msg(self):
        print('\nWELCOME TO HANGMAN!')
        print(f'\nThe word contains \033[1m{len(self.word)} letters\033[0m.\n')

    def init_progress(self):    # creates a list of underscores which represents un-guessed letters of the target word
        for i in range(len(self.word)):
            self.progress.append('_ ')

    def guess(self):
        print(f'\nYou have \033[1m{self.lives} lives\033[0m remaining.')
        print(f'\n{str().join(self.progress)}')

        if self.used_chars:     # if this isn't the first turn (i.e. the "used_chars" list is populated), then print it
            print(f'\nYou have used these letters:')
            print(f'{self.used_chars}\n')

        user_guess = input('\nPlease guess a letter: ').upper()

        while True:
            if not user_guess.isalpha():    # guess has to be a letter of the alphabet
                user_guess = input('\nPlease guess a \033[1m letter \033[0m of the alphabet: ').upper()
                continue

            if len(user_guess) != 1:    # users are only allowed to guess one letter at a time
                user_guess = input('\nPlease only guess \033[1m one letter \033[0m at a time: ').upper()
                continue

            elif user_guess in self.used_chars:     # make sure users don't use the same letter multiple times
                print('\nYou have already guessed that letter.')
                user_guess = input('\nPlease guess a different letter: ').upper()
                continue

            else:
                break

        if user_guess in self.word:
            print('\n\nCORRECT!\n')
            for idx, letter in enumerate(self.word):    # replaces the underscores in "self.progress" with the
                if user_guess == letter:                # guessed letter
                    self.progress[idx] = f'{letter} '
        else:
            print('\n\nINCORRECT!\n')
            self.lives -= 1

        self.guesses += 1
        self.used_chars.append(user_guess)

    def start_game(self):
        self.generate_word()
        self.starting_msg()
        self.init_progress()
        while True:
            self.guess()
            if self.lives < 1:
                print('\nYou lost!')
                print(f'\nThe word was \033[1m{str().join(self.word).upper()}\033[0m')
                break
            elif '_ ' not in self.progress:
                print(f'\n\033[1m{str().join(self.progress)}\033[0m')
                print(f'\nYou guessed the correct word with {self.guesses} guesses!')
                break
        print('\nTHANKS FOR PLAYING!')


if __name__ == "__main__":
    game = Hangman()
    game.start_game()
