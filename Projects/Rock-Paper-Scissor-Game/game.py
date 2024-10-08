import random

y = 1
while y == 1:
    rock = '''
      ___
  ---'   __)
        (___)
        (___)
        (__)
  ---._(__)
  '''

    paper = '''
      ___
  ---'   _)_
            __)
            ___)
           ___)
  ---.____)
  '''

    scissors = '''
      ___
  ---'   _)_
            __)
         ____)
        (__)
  ---._(__)
  '''
    game_images = [rock, paper, scissors]

    user_choice = int(
        input("""What do you choose? Type 0 for Rock, 1 
  for Paper or 2 for Scissors.\n"""))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number,you lose!")
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")
    print("""Do you want to play again?:
        1->Yes
        2->No""")
    y = int(input("Your Choice:"))
    if y != 1 and y != 2:
        print("You have entered an invalid value. Try again")
        y = 1
    if y == 2:
        print("Thanks for Playing!")
        break