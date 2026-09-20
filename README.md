🎲 S1X-Z3R0D1C364M3

S1X-Z3R0D1C364M3 is a simple command-line dice guessing game written in Python.

The player guesses the total of two six-sided dice, rolls both dice, and finds out whether their prediction was correct.

by 6-0

🎮 How to Play

Start SixZeroDiceGame.exe

Guess a number between 2 and 12

Press Enter to roll the first die

Press Enter again to roll the second die

Enter an amount of imaginary Sterling for the bet

The game reveals both dice and their combined total

Find out whether your guess was correct

Press Enter to play again

The game automatically returns to the beginning after each round.

⌨️ Controls

Enter — Continue, roll the dice, or start another game

F10 — Exit the game

🎲 The Game

The objective is simple:

Guess the combined total of two dice.

Each die produces a random value from 1 to 6, giving a possible total between 2 and 12.

Example:

Your guess: 9

First dice roll: ─» 4
Second dice roll: ─» 5

You have rolled a total count of: 9

🎉 Congratulations! You guessed correctly!


The betting system is purely fictional. The game does not involve real money.

🖥️ Standalone Windows Executable

A standalone Windows executable is provided as:

SixZeroDiceGame.exe

Python does not need to be installed to run the executable.

Download the .exe from the GitHub Releases section and run it.

🐍 Run From Python

The main source file is:

SixZeroDiceGame.py

Run it with:

python SixZeroDiceGame.py


Python 3.x is required.

🔨 Building the Executable

This project uses PyInstaller to create the standalone Windows executable.

Install PyInstaller:

python -m pip install pyinstaller


Build the executable:

python -m PyInstaller --onefile --name SixZeroDiceGame SixZeroDiceGame.py


The executable will be created inside:

dist/SixZeroDiceGame.exe

📁 Project Structure
SixZeroDiceGame/
│
├── SixZeroDiceGame.py
├── README.md
├── LICENSE
└── .gitignore


The compiled executable is distributed through GitHub Releases.

🔢 The Name
S1X-Z3R0D1C364M3

The project name uses leetspeak:

S1X    = SIX
Z3R0   = ZERO
D1C3   = DICE
64M3   = GAME


Which gives:

S1X-Z3R0D1C364M3


The 6-0 signature is part of the game's visual identity and appears in the ASCII artwork.

🎨 ASCII Dice

The game uses custom console ASCII artwork rather than a graphical interface.

The aim is to keep the game lightweight, simple and reminiscent of classic command-line games.

               ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
            ■                        ■   ■
          ■       ☺         ☺      ■      ■
        ■                        ■         ■
      ■      ☺         ☺       ■            ■
    ■                        ■               ■
  ■                         ■                 ■
 ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■                   ■
 ■                          ■         ☺         ■
  ■       ☺         ☺        ■                   ■
   ■                          ■                   ■
    ■                          ■                 ■
     ■            ☺             ■              ■
      ■                          ■           ■
       ■                          ■        ■
        ■        ☺         ☺       ■     ■
         ■                          ■  ■
 by 6-0    ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

⚙️ Requirements
Standalone .exe

Windows

No Python installation required

Python source

Python 3.x

Windows recommended for full F10 functionality

📜 License

See the LICENSE file included in this repository.

🎲 S1X-Z3R0D1C364M3

Guess the number. Roll the dice.

by 6-0
