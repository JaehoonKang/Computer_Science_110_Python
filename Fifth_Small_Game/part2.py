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

def main():
    
  print('★★★★★★★Lucky Seven Game★★★★★★★')

  # Input
  money_str = input('Please place your bet in positive whole dollars \
  OR press <Enter> to quit:')
  
  while money_str:

    # Validation Loop: test the input if the input is greater than 0
    while not (money_str.isdigit() and int(money_str) > 0):
        
      print('INVALID INPUT:  Input whole numbers greater than 0 ONLY')
      money_str = input('Please place your bet in positive whole dollars \
      OR press <Enter> to quit:')

    money = int(money_str)

    print("%4s %8s %10s" %('Roll','Value','Dollars'))

    # roll and pot setting
    roll = 0
    pot = {}
    
    while money !=0:
      
      # dice and sum of dices setting
      dice_1 = random.randrange (1,7)
      dice_2 = random.randrange (1,7)
      value = dice_1 + dice_2
      if value == 7:
        money += 4
        
      else:
        money -= 1
        
      roll += 1
      pot[roll] = money
      
      print("%4d  %6d  %10.2f" %(roll, value, money))
    
    print("You became broke after %d rolls" %roll)

    roll = max(pot, key=pot.get)
    max_money = pot[roll]
    print("You should have quit after %d rolls when you have $%.2f" \
            %(roll, max_money) )
      
    money_str = input('Please place your bet \
in positive whole dollars OR press <Enter> to quit:')
    
main()
