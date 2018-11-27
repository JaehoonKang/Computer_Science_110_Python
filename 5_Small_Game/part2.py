'''
Name Kang Jaehoon
Email jkang36@binghamton.edu
Assignment5 - 2
Lab# C60
CA Vlad Malcevic
Phone 9177246430
'''
'''
ANALYSIS
RESTATEMENT:

  The program simulates rolling a pair of dice for each turn
  If the sume of the dices equals 7, the player wins $4; otherwise,
  the player loses $1.
  This game continues until the pot is empty

OUTPUT to monitor:

  Decide each roll, dice value, money left
 
INPUT from keyboard:

  money_str(string): input('place your bet in whole number positive whole:')
  
GIVEN:

  DICE_MIN (int): 0 - the minimum value of the dice
  DICE_MAX (int): 6 - the maximum value of the dice

PROCESSING:

  Import required module: random

  Explain the purpose of this program to a user, using a print expression

  Get an input value from a user: input("please place your bet")

  Validate the input from a user (While loop)

  Once it passes the validation, convert it to an integer value

  Create two dices and using them, find the sume of two dices (value)

  Using a while loop (Continuation), decide if a user wins $4 or loses $1

  Every round, determin the table (roll, dice value, and money left)
  Also using the pot, find the max money the user could have gotten

  Ask the user if he continues the program (input)

FORMULAS:

'''
# IMPORT 
import random

# CONSTANTS
# Define minimum & maximum value of the dice 
DICE_MIN = 1
DICE_MAX = 6

# Design
def main():
    
  print('This is a game based on lucky seven')

  
  
  # Priming Read
  # Input: Get an input from a user for a bet
  money_str = input('Please place your bet in positive whole dollars \
  OR press <Enter> to quit:')

  # Continuation Loop:
  #   Keeping a program going until a user wants to quit(hit <Enter>)
  while money_str:

    # Validation Loop: to force the user to give a valid input
    #   Whether the input is an integer and is greater than 0
    while not (money_str.isdigit() and int(money_str) > 0):
        
      print('INVALID INPUT:  Input whole numbers greater than 0 ONLY')
      money_str = input('Please place your bet in positive whole dollars \
      OR press <Enter> to quit:')

    # Once the Validation is done, convert the value into an integer
    money = int(money_str)

    # Create a table for Roll, Value, and Dollars
    print("%4s %8s %10s" %('Roll','Value','Dollars'))

    
    # roll and pot setting
    # roll starts at 0 
    roll = 0
    # Using a dictionary for a pot
    pot = {}

    # While loop until money equals to 0
    while money !=0:
      
      # dice and sum of dices setting (value)
      dice_1 = random.randrange (DICE_MIN,DICE_MAX)
      dice_2 = random.randrange (DICE_MIN,DICE_MAX)
      value = dice_1 + dice_2

      # if value equals to 7
      if value == 7:
        money += 4
        
      else:
        money -= 1

      # roll increment by 1 each turn  
      roll += 1

      # putting a key and corresponding value in a dictionary
      pot[roll] = money

      # print out roll, value and money
      print("%4d  %6d  %10.2f" %(roll, value, money))
    
    print("You became broke after %d rolls" %roll)

    # using max() to find the maximum value of key and value in dictionary
    roll = max(pot, key=pot.get)

    # save the max value to max_Money
    max_Money = pot[roll]
    
    # Display the sentence with the calculated outcome with % specifiers
    print("You should have quit after %d rolls when you have $%.2f" \
            %(roll, max_Money) )
    
    # Continuation Read:
    #   Keeps the program going as long as user enters input
    money_str = input('Please place your bet \
in positive whole dollars OR press <Enter> to quit:')
    
main()
