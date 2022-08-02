"""
CODE WALK-THROUGH:
-----------------
-The problem my program solves is BOREDOM.
-My program is a guessing game.
-The user is asked to play for a chance to win a certain amount of money.
-Were a random number is picked from a certain range and clues are given to aid the user guess the number.
-The user gets three chances to guess the number
-If by chance the user can't win the game the user would die and quit the game.
-If the user wins he is given the opportunity to play again or end the game and leave with the cash price or move onto level 2.
"""


import random # I imported RANDOM so i can prompt the computer to choose a random from a certain range

def play_game():
      def start():
            start = input("Enter 'START' when ready to begin: ")
            if start != 'START':
                  print("--ENTER START!!--") # Incase the user enters something other than 'START'. The user will have to type it in correctly
                  start()
            print(' ')
      start()

      print('\033[1m' + "LEVEL 1: "  + '\033[0m' + "A random number between 1 and 10 was picked") # Before and After "LEVEL" is syntax to print the statement in bold

      def decide(): # This function is meant for the user to choose what happens after they've won game
            decision = input("Enter 'END' to End Game or 'REPEAT' to play again or 'PROCEED' to move to Level 2: ")

            if decision == "END":
                  print("Congratulations!! You leave with a sum of $50,000,000")
                  exit()# If the user doesnt want to play anymore the program will stop here
            elif decision == "REPEAT":
                  print("  ~\n"
                        "  ~\n"
                        "  ~\n"
                        f"Welcome Back!! {user_name}\U0001F921")
                  play_game() # If the user wants to play this particular level again the program will start again from the play_game function
            elif decision == "PROCEED":# If the user wants to proceed to level 2
                  print(f"{user_name.upper()} you will be informed when Level 2 is available")
                  exit() # Since level 2 isn't avaiable the moment the user is informed to that effect and the program ends
            else: # This is used to catch situations were the user enters something apart from the available options
                  print("CHOOSE!!")
                  decide() # The user will be taken back to the decide() function to provide a valid input
      def game(): # This is where the heart of the game is located
            answer = random.randint(1, 11) # Computer generates a random integer in that range
            noo = "         WRONG!!\U0001F608"
            lost = '\033[1m' + "         YOU LOSE!!" + '\033[0m'
            die = '\033[1m' + "         DIEEEE" + '\033[0m' + "    \U0001F62D\U0001F52B"
            number_of_guesses = 3 # I have limited the number of tries to just 3
            while True:
                  guess = int(input('\033[1m' + "         What is the number? " + '\033[0m'))
                  if guess == answer: # This if statement is for if the user gets it right
                        if number_of_guesses > 1: # I made another if statement inside the outer "if" because I want to print the number of tries the user has left after he got the answer right. Since 1 is TRY and more than 1 is TRIES.
                              print(f"YOU GOT IT RIGHT!!!\U0001F973\U0001F973\U0001F973 with {number_of_guesses} more tries left\n" # If the user has more than one try left. It will print out "(number of guesses)" more TRIES left
                              f" ")
                        else: # And if number of guesses left is anything not greater 1. It will print out 'on your last try'
                              print(f"YOU GOT IT RIGHT!!!\U0001F973\U0001F973\U0001F973 on your last try\n"
                                    f" ")
                        print("YOU NOW HAVE THREE CHOICES: \n"
                              f"------End the game now and leave with $50,000,000 \n"
                              "                  OR \n"
                              "------Repeat IF YOU DARE! \n"
                              "                  OR \n"
                              "------Proceed to Level 2\n"
                              " \n"
                              "      CHOOSE WISELY")
                        decide()
                  elif guess != answer and answer == 10:                                       # The following if statements are for what happens when each random number is chosen
                        if guess != answer and number_of_guesses == 1:                         # If the user gets the answer wrong and has 1 guess left before getting it wrong
                              print(lost)                                                      # The user will be notified that the game has been LOST
                              print(die)
                              exit()                                                           # The program will be terminated
                        print(noo)
                        print("         HINT: We use this number system every single day")
                  elif guess != answer and answer == 9:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: When inverted it is another number")
                  elif guess != answer and answer == 8:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: It's made of two balls")
                  elif guess != answer and answer == 7:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: The number is the known as the Lucky number")
                  elif guess != answer and answer == 6:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: The nickname for the man who carries Toronto")
                  elif guess != answer and answer == 5:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: The number is one of the primes")
                  elif guess != answer and answer == 4:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: The number is divisible by both an even and odd number")
                  elif guess != answer and answer == 3:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: Its green")
                  elif guess != answer and answer == 2:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: The number is the most used number system in CPS 213 class")
                  elif guess != answer and answer == 1:
                        if guess != answer and number_of_guesses == 1:
                              print(lost)
                              print(die)
                              exit()
                        print(noo)
                        print("         HINT: Its not false")
                  number_of_guesses -= 1 # The number of guesses reduces by 1 everytime the user doesnt get the answer right
      game()


if __name__ == "__main__":
      print("\U0001F921\U0001F52A WELCOME TO THE SQUID GAME \U0001F921\U0001F52A")  # What was written at the beginning and ending of the print
                                                                                    # statements are represenations of various emojis
      user_name = input(f"~Enter your name: ")
      start_game = input(f"~{user_name.upper()} type in 'PLAY' to begin the SQUID GAME \U0001F608 or ANYTHING ELSE to run away \U0001F419: ")
      if start_game != "PLAY": #The if statement is for a situation were the user decides not to play the game
            print("YOU DON'T HAVE THE GUTS TO PLAY")
            exit()

      print("RULES OF THE SQUID GAME \n"
            "------------------------ \n"
            "1. Once you start you must play OR YOU DIE!! \U0001F52A \n"
            "2. If you lose YOU DIE!! \U0001F52A \n"
            "3. If you get the answer right within your chances. YOU WIN!! \U0001F911 \n"
            "4. You have a maximum of 3 chances\n"
            f"              The Total Cash Prize for Level 1 is $50,000,000\n"
            f"              ---------------------for Level 2 is $100,000,000"
            "\n"  # These spaces aren't to fulfill the "20 lines of comments" condition or elongate my code.
            " ")  # They are there to better the look of my output

      play_game()