'''
Kang Jaehoon
jkang36@binghamton.edu
917-724-6430
C60
Assignment 3-2
'''
'''
ANALYSIS

RESTATEMENT:

  Ask a user to enter the year and decide if this year is a leap year or not
  
OUTPUT to monitor:

 num_year (int) -  either a leap year or just a year
 
INPUT from keyboard:

 num_year_str = input("Enter a year: ")

 num_year (int) - int(num_year_str)

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

  num_year % 4 == 0

  num_year % 100 == 0

  num % 400 == 0
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

# Explain purpose of program to user
# This program to check if a input year is a leap year or not

print("This program determines if a given year is a leap year or not\n")

# DESIGN

def main():
    
    num_year_str = input("Enter a year: ")
    
    num_year = int(num_year_str)

#if-else statement whether the year is a leap year 

    # if the year is a leap
    
    if (num_year % FOUR == ZERO) and  ( num_year % HUNDRED != 0 ) or \
       ( num_year % FOUR_HUNDRED == ZERO):
           
        print ("%d is a leap year \n" %num_year)
        
    # else
    
    else:
        
        print ("%d is not a leap year \n" %num_year)


# Using for-loop in range from 1800 to 2100, increased by 10

    for num_year in range (STARTING_YEAR, ENDING_YEAR, 10):
        
         if (num_year % FOUR == ZERO) and  ( num_year % HUNDRED != 0 ) or\
            ( num_year % FOUR_HUNDRED == ZERO):
                
           print ("%d is a leap year \n" %num_year)
           
         else:
             
           print ("%d is not a leap year\n" %num_year)
          
main()
