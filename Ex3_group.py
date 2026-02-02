# -------------------------------------------
# Exercise 3: Group Exercise
# -------------------------------------------
#
# GOAL:
# 1. Create a Python program collaboratively in groups of 2–3.
# 2. Practise using Variables, Input, and Decision Making (if/elif/else).
# 3. Master the "Relay Race" style of coding using Git.
#
# CONCEPT:
# Collaborative coding involves multiple developers working on the same codebase.
# - You will build one program together, layer by layer.
# - You must use Git to sync your code so everyone has the latest version.
#
# PAIR PROGRAMMING RULES:
# - The DRIVER types the code.
# - The NAVIGATOR reads the instructions and guides the driver.
# - You will SWITCH roles and computers after every task!
# -------------------------------------------


# -------------------------------------------
# Task 1: Personal Information
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: The Profile Builder\n"
    + "-------------------------------------------")

# Note: Read all of the instructions below first before starting!

# TODO:
# 1. Ask the user for their **name**.
# 2. Ask the user for their **favourite colour**.
# 3. Store these in descriptive variables.
# 4. Print a message using an f-string (e.g., "Sam likes Red").

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Open the terminal.
# 3. Run:
#    git add Ex3_group.py
#    git commit -m "Completed Task 1"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: Simple Decision (The Guessing Game)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer. Get the latest code!
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: The Guessing Game\n"
    + "-------------------------------------------")

# Note: We are avoiding age checks to keep the logic purely mathematical.

# TODO:
# 1. Create a variable `secret_number` and set it to 7 (or any number you like).
# 2. Ask the user to guess a number (Input).
#    (Remember to convert the input to an integer!)
# 3. Use an if-else statement:
#    - IF the guess is equal (==) to the secret number: Print "You won!"
#    - ELSE: Print "Wrong guess, try again."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex3_group.py
#    git commit -m "Completed Task 2"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: Multiple Conditions (High Scores)
# -------------------------------------------
# INSTRUCTION: Get the code from the previous Driver.
# 1. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: The High Score Battle\n"
    + "-------------------------------------------")

# Scenario: We need to compare the scores of two players.

# TODO:
# 1. Ask for **Player 1's Score** (integer).
# 2. Ask for **Player 2's Score** (integer).
# 3. Use if-elif-else to compare them:
#    - IF Player 1 > Player 2: Print "Player 1 wins!"
#    - ELIF Player 1 == Player 2: Print "It's a draw!"
#    - ELSE: Print "Player 2 wins!"

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex3_group.py
#    git commit -m "Completed Task 3"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Weather Station (Logical Operators)
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "Extension 1: The Weather Station\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for the temperature (integer).
# 2. Ask the user if it is raining (Input "yes" or "no").
# 3. Use `and` / `or` logic:
#    - IF temp < 10 AND raining == "yes": Print "Stay inside, it's cold and wet."
#    - ELSE: Print "You can go outside."

# Write your code below:


# Extension 2: The Quiz Master
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: The Quiz Master\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user a general knowledge question (e.g. "What is the capital of France?").
# 2. Use if-elif-else to handle the answer:
#    - IF exact match ("Paris"): Print "Correct!"
#    - ELIF match with wrong case ("paris"): Print "Correct, but capitalize it next time."
#    - ELSE: Print "Wrong answer."

# Write your code below:


# Extension 3: The Adventure Game (Nested Logic)
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: The Adventure Game\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user to choose a door: "Left" or "Right".
# 2. IF they choose "Left":
#    - Ask a second question: "Swim" or "Wait"?
#    - Print different outcomes for each choice.
# 3. ELIF they choose "Right":
#    - Print "You fell into a trap. Game Over."
# 4. ELSE:
#    - Print "You didn't move. Nothing happened."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Open terminal.
# 3. Run:
#    git add Ex3_group.py
#    git commit -m "Completed all extensions"
#    git push origin main
#
# Check GitHub to see your combined work!
# -------------------------------------------
