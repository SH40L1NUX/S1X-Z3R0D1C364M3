import random
import ctypes
import msvcrt
import sys
import time


# ============================================================
# SIXZERODICEGAME
# Press F10 at any time to exit the game.
# ============================================================

def f10_pressed():
    """
    Checks whether F10 has been pressed.
    F10 virtual-key code = 0x79.
    """
    return bool(ctypes.windll.user32.GetAsyncKeyState(0x79) & 0x8000)


def check_exit():
    """
    Exits the game if F10 is pressed.
    """
    if f10_pressed():
        print("\n\nF10 pressed. Exiting SixZeroDiceGame...")
        time.sleep(1)
        sys.exit(0)


def wait_for_enter(prompt):
    """
    Waits for the user to press Enter while also checking F10.
    """
    print(prompt, end="", flush=True)

    while True:
        check_exit()

        if msvcrt.kbhit():
            key = msvcrt.getwch()

            if key == "\r":
                print()
                return

        time.sleep(0.05)


def get_guess():
    """
    Gets a valid guess between 2 and 12.
    """
    while True:
        check_exit()

        print(
            "Guess a number within a range of 2 to 12 "
            "as a sum total for two rolls of a dice."
        )

        print("Press F10 at any time to exit.")

        print()

        guess_text = input("Your guess: ")

        check_exit()

        try:
            guess = int(guess_text)

            if 2 <= guess <= 12:
                return guess

            print("\nPlease enter a number between 2 and 12.\n")

        except ValueError:
            print("\nPlease enter a whole number.\n")


def display_title():
    """
    Displays the SixZeroDiceGame title screen.
    """
    print("─────────────────────────────────────────────────────────────────────────")

    print("               ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■        ")
    print("            ■                        ■   ■      ")
    print("          ■       ☺         ☺      ■      ■     ")
    print("        ■                        ■         ■    ")
    print("      ■      ☺         ☺       ■            ■   ")
    print("    ■                        ■               ■  ")
    print("  ■                         ■                 ■ ")
    print(" ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■                   ■")
    print(" ■                          ■         ☺         ■")
    print("  ■       ☺         ☺        ■                   ■")
    print("   ■                          ■                   ■")
    print("    ■                          ■                 ■")
    print("     ■            ☺             ■              ■")
    print("      ■                          ■           ■")
    print("       ■                          ■        ■")
    print("        ■        ☺         ☺       ■     ■")
    print("         ■                          ■  ■")
    print(" by 6-0    ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")

    print("─────────────────────────────────────────────────────────────────────────")
    print("                    S1X-Z3R0D1C364M3")
    print("─────────────────────────────────────────────────────────────────────────")
    print()


def play_game():
    """
    Runs one complete game.
    """

    display_title()

    # --------------------------------------------------------
    # GUESS
    # --------------------------------------------------------

    guess = get_guess()

    print()
    print(
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    )

    # --------------------------------------------------------
    # FIRST DICE
    # --------------------------------------------------------

    wait_for_enter("Press Enter to roll a dice: ")

    check_exit()

    print("♫♫-♫---♫")
    print("*Rolls a dice*")

    print(
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    )

    dice1 = random.randint(1, 6)

    # --------------------------------------------------------
    # SECOND DICE
    # --------------------------------------------------------

    wait_for_enter("Press Enter again to roll another dice: ")

    check_exit()

    print("♫-♫♫-♫-♫-♫♫---♫")
    print("*Rolls another dice*")

    print(
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    )

    # --------------------------------------------------------
    # IMAGINARY BET
    # --------------------------------------------------------

    while True:
        check_exit()

        money = input(
            "How much of imaginary money do you want to lose "
            "on this bet in Sterling? - "
        )

        check_exit()

        # The money is deliberately imaginary and isn't used.
        if money.strip():
            break

        print("Please enter an amount.")

    print(
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    )

    # --------------------------------------------------------
    # SECOND ROLL
    # --------------------------------------------------------

    dice2 = random.randint(1, 6)

    total = dice1 + dice2

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    print("First dice roll: ─» " + str(dice1))

    print("─────────────────────────────────────────────────────────────────────────")

    print("Second dice roll: ─» " + str(dice2))

    print("─────────────────────────────────────────────────────────────────────────")

    print(
        "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    )

    print("You guessed: " + str(guess))
    print("You have rolled a total count of: " + str(total))

    print("─────────────────────────────────────────────────────────────────────────")

    if guess == total:
        print("Cg. Legend! Now lets try time the stock market and predict it all.")
    else:
        print("Flop! Better luck next time!")

    print("─────────────────────────────────────────────────────────────────────────")


def main():
    """
    Main game loop.

    When a game finishes, the program returns to the
    beginning automatically.
    """

    while True:
        check_exit()

        play_game()

        print()
        print("Try again?.")
        print("Press F10 at any time to exit this masterpiece of coding.")
        print()

        wait_for_enter("Press Enter to play Six Zero Roll a Dice again: ")

        print("\n" * 3)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\nSixZeroDiceGame closed.")