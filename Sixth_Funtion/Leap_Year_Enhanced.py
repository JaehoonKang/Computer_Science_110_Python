'''
Name Kang Jaehoon
email jkang36@binghamton.edu
Assignment 6 - 1
Lab# C60
CA Vlad Malcevic
Phone 9177246430
'''
'''
ANALYSIS

RESTATEMENT:

  Ask a user to enter the year and decide if this year is a leap year or not
  
OUTPUT to monitor:

 num_year (int) -  either a leap year or just a year
 
INPUT from keyboard:

 num_year (int) - input("Enter a year: ")

GIVEN:

  FOUR = 4

  ZERO = 0

  HUNDRED = 100

  FOUR_HUNDRED = 400

PROCESSING:

  Import required module: math

  Explain a purpose of this program to a user, using a print expression

  Define four constants: FOUR, ZERO, HUNDRED, FOUR_HUNDRED

  Get an input value from a user: input("Enter a year: ")

  Decide if the input is a leap year using if-else statment

  With numbers increased by 10 From 1800 to 2100,
  Decide the number is a leap year

FORMULAS:

  To see a leap year:
  
    num_year % 4 == 0

    num_year % 100 == 0

    num_year % 400 == 0
'''


# IMPORTS

import math

# CONSTANTS

FOUR = 4

ZERO = 0

HUNDRED = 100

FOUR_HUNDRED = 400

STARTING_YEAR = 1800

ENDING_YEAR = 2101

# Add Constant List to my leap year program

TEST_EDGE_DATA_LIST = \
[1599,1600,1601,1602,1603,1604,1605, 1799,1800,1801,1802,1803,1804,1805]

# Explain purpose of program to user
# This program to check if a input year is a leap year or not

print("This program determines if a given year is a leap year or not \n")

# DESIGN

# Define a Function to decide if the year is an integer or > 0
def is_positive(year):
  return year.isdigit() and int(year) > 0

# Define a Function to see if the year is a leap year
def is_leap_year(year):
  return (year % FOUR == ZERO) and (year % HUNDRED != ZERO) or \
(year % FOUR_HUNDRED == ZERO)

def main():

  # Explain the program
  print("This program is to determine if the year put in is a leap year")

  print("Please enter a year you want to check if it is a leap year")

  # Priming Read:
  #  Input: get an input from a user to determine a year
  num_year = input("Enter year in whole numbers or press <Enter> to quit: ")

  # Continuation Loop:
  #   Keeping a program going until a user wants to quit(hit <Enter>)
  while num_year:

    # Validation Loop: to force the user to give a valid input
    #   Whether the input is an integer and is greater than 0
    while not is_positive(num_year):
      print("INVALID INPUT:  Input whole numbers greater than 0 ONLY")
      num_year = input("Enter year in whole numbers or press <Enter> to quit: ")

    # Convert it to an integer and save it in a variable, year
    year = int(num_year)

    # Using another variable to determin a leap year
    criterian = (year % FOUR == ZERO) and (year % HUNDRED != ZERO) or \
  (year % FOUR_HUNDRED == ZERO)

    # Using Ternary Operator (Expression) to simplify the sentence       
    print ("%d %s" %(year, ("is a leap year" if criterian else "is not a leap year")))
    
    ## Debug Statement
    ##  
    
    num_year = input("Enter year in whole numbers or press <Enter> to quit: ")
  '''  
  # After-classs modified & simplified addition

  criterian = (num_year % FOUR == ZERO) and (num_year % HUNDRED != ZERO) or \
  (num_year % FOUR_HUNDRED == ZERO)

  # Using Ternary Operator (Expression) to simplify the sentence         
  print ("%s %s  \n" %(num_year, ("is a leap year" if criterian else "is not a leap year")))


# Using for-loop in range from 1800 to 2100, increased by 10

  for year_check in range (STARTING_YEAR, ENDING_YEAR, 10):
        
    criterian = (year_check % FOUR == ZERO) and (year_check % HUNDRED != ZERO) or \
    (year_check % FOUR_HUNDRED == ZERO)

    # Using Ternary Operator (Expression) to simplify the sentence       
    print ("%s %s" %(year_check, ("is a leap year" if criterian else "is not a leap year")))

# Using addiontional years (list) to decide if year in the list is leap year

  print()  
  for year in TEST_EDGE_DATA_LIST:
      
    criterian = (year % FOUR == ZERO) and (year % HUNDRED != ZERO) or \
    (year % FOUR_HUNDRED == ZERO)
    
    # Using Ternary Operator (Expression) to simplify the sentence       
    print ("%s %s" %(year, ("is a leap year" if criterian else "is not a leap year")))
 '''         
main()
