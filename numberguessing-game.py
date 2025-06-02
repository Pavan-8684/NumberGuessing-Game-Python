from random import randint

logo = r"""
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("📈 Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("📉 Too low.")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was {actual_answer} 🥳")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"\nYou have {turns} attempt(s) remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("❌ Please guess a number between 1 and 100.")
            continue

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("😞 You've run out of guesses, you lose. Better luck next time!")
            return
        elif guess != answer:
            print("🔄 Guess again.")


game()
