'''
Name: Jaehoon Kang
email: jkang36@binghamton.edu
Lab Section and CA Name
Lab #C60
'''

## Do not write anything past column 78
## Go to next line instead (no wrapping!)
## USE MEANINGFUL NAMES!
## variables will use lower_snake_case
## constants will use UPPER_SNAKE_CASE

'''
ANALYSIS

RESTATE the problem clearly and without ambiguity

  Ask a user how many of different types of coin they have
  and convert it to the total value in dollars

OUTPUT to monitor:
  out_variable_name1 (variable_type) - description (only when needed)
  out_variable_name2 (variable_type) - description
  
  total_dollars (int) - the total value in dollars 
  . . .

INPUT from keyboard:
  (Note:  you can list converted variables here,
          rather than clutter the section with
          string versions that must be converted)
  in_variableName1 (variable_type) - description (only when needed)

  quarter_count_str = input("Please enter the number of quarters you have: ")
  dime_count_str = input("Please enter the number of dimes you have: ")
  nickel_count_str = input("Please enter the number of nickels you have: ")
  penny_count_str = input("Please neter the number of pennies you have: ")
  
  . . .

GIVENS (i.e., program constants):

  NAMED_CONSTANT1 (variable_type) - value
  NAMED_CONSTANT2 (variable_type) - value
  
  # Your code here:
  QUARTER_VALUE (int) => 25
  PENNY_VALUE (int) => 1
  NICKEL_VALUE (int) => 5
  DIME_VALUE (int) => 10

  
  TO_DOLLAR (int) => 100

PROCESSING:
  Get input, Convert str input to int values
  Find total value of each type of coin:  coin_type_value * coin_type_count
    (substitute actual coin_type:  quarter_value, quarter_count, etc.)
  Convert int value to dollar value (will be float):  total_value / 100
    (make 100 a named constant)
  Display output

  print("The total amount of change you have in dollars is $%.2f" %
        total_dollars)
'''

# CONSTANTS 
QUARTER = 25  # go ahead and code the remaining constants
DIME = 10
NICKEL = 5
PENNY = 1

## BRIEF description of overall program:
# This program outputs the total amount of change that a user has in dollars
# given the count of each type of coin

def main():
  ## START by giving the overall flow of your program in comments,
  ##   then interleave your code

  # Explain purpose of program to user
  print("This program will print out the total amount of change " +
        "you have in dollars when you provide a count of each type of coin")

  # Ask user for number of coins they have
  ## Start with quarters, end with pennies
  # Note constraints: no dollar, half-dollar coins
  quarter_count_str = input("Please enter the number of quarters you have:  ")
  dime_count_str = input("Please enter the number of dimes you have: ")
  nickel_count_str = input("Please enter the number of nickels you have: ")
  penny_count_str = input("Please neter the number of pennies you have: ")
  ## Input the rest here 
  

  # Convert str data to int
  quarter_count = int(quarter_count_str)
  dime_count = int(dime_count_str)
  nickel_count = int(nickel_count_str)
  penny_count = int(penny_count_str)
  ## Convert the rest here

  # Multiply the value of each type of coin by it's count and sum each result
  total_cents = (QUARTER * quarter_count) + \
                (DIME * dime_count) + \
                (NICKEL * nickel_count) + \
                (PENNY * penny_count)
  ## finish this 

  # Convert to dollars (float)
  total_dollars = (total_cents) / 100 ## finish this

  # Display labeled and formatted amount in dollars
  print("The total amount of change you have in dollars is $%.2f" %
        total_dollars)
  

main()
