'''
Name Kang Jaehoon
Email jkang36@binghamton.edu
Assignment5 - 3
Lab# C60
CA Vlad Malcevic
Phone 9177246430
'''
'''
ANALYSIS
RESTATEMENT:

  Write a complete program that iteratively computes the amount of money
  a person would earn over a period of time

OUTPUT to monitor:

  The day and the salary that was for the day
 
INPUT from keyboard:

  the number of days(string): input("Enter the number of days: ")
  
GIVEN:

  FIRST = 1 - First Day
  DOLLAR = 100 - to convert to a dollar

PROCESSING:

  Explain the purpose of this program to a user, using a print expression

  Get an input value from a user: input("Enter the number of days:")

  Validate the input from a user (While loop)

  Once it passes the validation, convert it to an integer value

  Using for loop, find the value for each day and salary

  Every round, determin the table (roll, dice value, and money left)
  Also using the pot, find the max money the user could have gotten

  Ask the user using a while loop if he continues the program (input)

FORMULAS:

'''

# Constant
FIRST = 1
DOLLAR = 100

# Design
def main():

    # Present the purpose of the program
    print("Days must be a positive value greater than zero")

    # Priming Read;
    #  Get an input from a user for how many days they want to compute
    days_str = input("Enter the number of days \
for which salary is to be computed:  ")

    # Continuation Loop:
    #   Keeping a program going until a user wants to quit(hit <Enter>) 
    while days_str:
        
      # Validation Loop: to force the user to give a valid input
      #   To determin whether the input is an integer or greater than 0
      while not (days_str.isdigit() and int(days_str) > 0):
        print("Days must be a positive value greater than zero")  
        days = input("Enter the valid number of days:  ")
        
      # Once the Validation is done, convert the value into an integer 
      days = int(days_str)  
      
      # Create a table for Day and Pay
      print("%6s %63s" %('Day', 'Pay'))
      print(70 *"-")

      # Display the first day
      print("%6d %62d" %(FIRST, FIRST)) 

      # Define a value as total for the total amount of money
      total = 0

      # Using a for-loop to find each day and corresponding dollar
      #   until the value meets the day the user inputs
      for inc in range(FIRST, days):
          
        # Each day, the amount doubles
        amount = 2**inc  
        # Add the amount to the total money  
        total += amount
        # Display each day and a corresponding the money
        print("%6d   %60d" %(inc +1, amount))
        
      print("")

      # Convert it to a dollar by dividing it by DOLLAR(100)
      dollar = (total + 1) / DOLLAR

      # Display the total amount and the last day
      print("In %d days a penny grows to $%9.2f" %(days, dollar))
      
      # Continuation Read:
      #   Keeps the program going as long as user enters input
      days_str = input("Enter the number of days \
for which salary is to be computed:  ")

main()
