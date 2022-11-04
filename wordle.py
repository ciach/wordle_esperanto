""" this is a wordle clone to play with esperanto words"""
import random
import sys
from rich.console import Console


def read_random_word(filename):
    """read a random word from a file"""
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().split()
        return random.choice(words)


if __name__ == "__main__":
    console = Console()
    word_to_guess = read_random_word("czap-6.txt")
    print(f"\n debugging: {word_to_guess} \n")

    for _ in range(6):
        guess = input("Guess a word: ").upper()
        if len(guess) != len(word_to_guess):
            print("Wrong length")
        if guess == word_to_guess:
            print("You win!")
            sys.exit(0)
        for item, letter in enumerate(guess):
            if guess[item] == word_to_guess[item]:
                console.print(guess[item], end=" ", style="bold green")
            elif guess[item] in word_to_guess:
                console.print(guess[item], end=" ", style="yellow")
            else:
                print("_", end=" ")
