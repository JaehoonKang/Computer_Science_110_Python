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

  FIRST = 1
  DOLLAR = 100

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

    print("Days must be a positive value greater than zero")
    days_str = input("Enter the number of days \
for which salary is to be computed:  ")

    while days_str:
        
      # Validation Loop
      while not (days_str.isdigit() and int(days_str) > 0):
        print("Days must be a positive value greater than zero")  
        days = input("Enter the valid number of days:  ")
      # Convert to an integer  
      days = int(days_str)  
      
      
      print("%6s %63s" %('Day', 'Pay'))
      print("-------------------------------------------------------------\
----------")
      print("%6d %62d" %(FIRST, FIRST)) 
      
      total = 0
      for inc in range(FIRST, days):
        amount = 2**inc  
        total += amount
        print("%6d   %60d" %(inc +1, amount))
        
      print("")
      dollar = (total + 1) / DOLLAR
      print("In %d days a penny grows to $%9.2f" %(days, dollar))  

      days_str = input("Enter the number of days \
for which salary is to be computed:  ")

main()
