from random import randint

Alpha= randint(1, 10)

def play_game():
    attempts = 3  
  
    while attempts > 0:
        userNumber = int(input('Guess the Number: '))
        
        if userNumber == Alpha:
            print("Congratulations! You Won!")
            break
        elif attempts == 1:
            print(f"Sorry, you've run out of attempts. The correct number was {Alpha}.")
            break
        else:
            print("Sorry, that's not the correct number. Try again.")
        
        attempts -= 1
   
play_game()
