'''
Name
email
Assignment4
Lab section#
CA name
'''

'''
RESTATEMENT:
  Display tax for single and married filers given set of incomes

OUTPUT to monitor:
  marital_status[status] (str)
  total_income[status][income] (float)
  tax (float)

GIVEN:
  marital_status (str) - ['single', 'married']
  total_income[status][income] (float):
    [[0,9075, 9076, 36900, 36901, 89350, 89351,
      186350, 186351, 405100, 405101, 406750, 406751],
     [0, 18150, 18151, 73800, 73801, 148850, 148851,
      226850, 226851,  405100, 405101, 457600, 457601]]
  Define constants below
  
  tax rate (float):
    [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

FORMULA:
  tax = base tax amount for bracket
          + (tax rate for bracket * (total_income[status][income]
          - base total_income[status][income] level for bracket))
'''

# No MAGIC numbers!
# CONSTANTS

# base total_income[status][income] levels
# for single and married tax brackets
SINGLE_BRACKET0 = 0
SINGLE_BRACKET1 = 9075
SINGLE_BRACKET2 = 36900
SINGLE_BRACKET3 = 89350
SINGLE_BRACKET4 = 186350
SINGLE_BRACKET5 = 405100
SINGLE_BRACKET6 = 406750

MARRIED_BRACKET0 = 0
MARRIED_BRACKET1 = 18150
MARRIED_BRACKET2 = 73800
MARRIED_BRACKET3 = 148850 
MARRIED_BRACKET4 = 226850
MARRIED_BRACKET5 = 405100
MARRIED_BRACKET6 = 457600

# Define base tax amounts for single and married tax brackets
BASE_SINGLE0 = 0
BASE_SINGLE1 = 907.50
BASE_SINGLE2 = 5081.25
BASE_SINGLE3 = 18193.75
BASE_SINGLE4 = 45353.75
BASE_SINGLE5 = 117541.25
BASE_SINGLE6 = 118118.75

BASE_MARRIED0 = 0
BASE_MARRIED1 = 1815
BASE_MARRIED2 = 10162.5
BASE_MARRIED3 = 28925
BASE_MARRIED4 = 50765
BASE_MARRIED5 = 109587.5
BASE_MARRIED6 = 127962.5

# Define tax rate applied to total_income[status][income] over
# base total_income[status][income] of given tax bracket
TAX_RATE1 = 0.1
TAX_RATE2 = 0.15
TAX_RATE3 = 0.25
TAX_RATE4 = 0.28
TAX_RATE5 = 0.33
TAX_RATE6 = 0.35
TAX_RATE7 = 0.396


# This progam displays the simple tax for single and married
# filers given a set of incomes
def main():
  # Explain what program does
  print(
    "This program computes a simple tax table for single and married filers")

  # Define marital status and income data
  marital_status = ['single', 'married']
  total_income = [[SINGLE_BRACKET0,SINGLE_BRACKET1, SINGLE_BRACKET1 + 1,
                   SINGLE_BRACKET2, SINGLE_BRACKET2 + 1,
                   SINGLE_BRACKET3, SINGLE_BRACKET3 + 1,
                   SINGLE_BRACKET4, SINGLE_BRACKET4 + 1,
                   SINGLE_BRACKET5, SINGLE_BRACKET5 + 1,
                   SINGLE_BRACKET6, SINGLE_BRACKET6 + 1],
                  [MARRIED_BRACKET0, MARRIED_BRACKET1, MARRIED_BRACKET1 + 1,
                   MARRIED_BRACKET2, MARRIED_BRACKET2 + 1,
                   MARRIED_BRACKET3, MARRIED_BRACKET3 + 1,
                   MARRIED_BRACKET4, MARRIED_BRACKET4 + 1,
                   MARRIED_BRACKET5, MARRIED_BRACKET5 + 1,
                   MARRIED_BRACKET6, MARRIED_BRACKET6 + 1]]

  # loop through single, then married categories
  for i in range(len(marital_status)):
    status = marital_status[i]
    # loop thru income brackets - will go through single first, then married
    for j in range(len(total_income[0])):
      income = total_income[i][j]
     
      # Use nested and chained conditionals to compute tax
      ### YOUR CODE HERE ###

      # To compute data for Single when i equals 0
      if i == 0:    
      
        if (income >= SINGLE_BRACKET0) and (income < SINGLE_BRACKET1):
          tax = BASE_SINGLE0
          
        elif (income >= SINGLE_BRACKET1) and (income < SINGLE_BRACKET2):
          
          if income == SINGLE_BRACKET1:
            tax = BASE_SINGLE1
          else:
            tax = BASE_SINGLE1 + (income - SINGLE_BRACKET1) * TAX_RATE2
            
        elif (income >= SINGLE_BRACKET2) and (income < SINGLE_BRACKET3):
          
          if income == SINGLE_BRACKET2:
            tax = BASE_SINGLE2
          else:
            tax = BASE_SINGLE2 + (income - SINGLE_BRACKET2) * TAX_RATE3
            
        elif (income >= SINGLE_BRACKET3) and (income < SINGLE_BRACKET4):
          
          if income == SINGLE_BRACKET3:
            tax = BASE_SINGLE3
          else:
            tax = BASE_SINGLE3 + (income - SINGLE_BRACKET3) * TAX_RATE4
            
        elif (income >= SINGLE_BRACKET4) and (income < SINGLE_BRACKET5):
          
          if income == SINGLE_BRACKET4:
            tax = BASE_SINGLE4
          else:
            tax = BASE_SINGLE4 + (income - SINGLE_BRACKET4) * TAX_RATE5

        elif (income >= SINGLE_BRACKET5) and (income < SINGLE_BRACKET6):
          
          if income == SINGLE_BRACKET5:
            tax = BASE_SINGLE5
          else:
            tax = BASE_SINGLE5 + (income - SINGLE_BRACKET5) * TAX_RATE6

        else:
          
          if income == SINGLE_BRACKET6:
            tax = BASE_SINGLE6
          else:
            tax = BASE_SINGLE6 + (income - SINGLE_BRACKET6) * TAX_RATE7
            
      # To compute data for Married when i equals 1      
      else:
        
        if (income >= MARRIED_BRACKET0) and (income < MARRIED_BRACKET1):
          tax = BASE_MARRIED0
          
        elif (income >= MARRIED_BRACKET1) and (income < MARRIED_BRACKET2):
          
          if income == MARRIED_BRACKET1:
            tax = BASE_MARRIED1
          else:
            tax = BASE_MARRIED1 + (income - MARRIED_BRACKET1) * TAX_RATE2
            
        elif (income >= MARRIED_BRACKET2) and (income < MARRIED_BRACKET3):
          
          if income == MARRIED_BRACKET2:
            tax = BASE_MARRIED2
          else:
            tax = BASE_MARRIED2 + (income - MARRIED_BRACKET2) * TAX_RATE3
            
        elif (income >= MARRIED_BRACKET3) and (income < MARRIED_BRACKET4):
          
          if income == MARRIED_BRACKET3:
            tax = BASE_MARRIED3
          else:
            tax = BASE_MARRIED3 + (income - MARRIED_BRACKET3) * TAX_RATE4
            
        elif (income >= MARRIED_BRACKET4) and (income < MARRIED_BRACKET5):
          
          if income == MARRIED_BRACKET4:
            tax = BASE_MARRIED4
          else:
            tax = BASE_MARRIED4 + (income - MARRIED_BRACKET4) * TAX_RATE5

        elif (income >= MARRIED_BRACKET5) and (income < MARRIED_BRACKET6):
          
          if income == MARRIED_BRACKET5:
            tax = BASE_MARRIED5
          else:
            tax = BASE_MARRIED5 + (income - MARRIED_BRACKET5) * TAX_RATE6

        else:
          
          if income == MARRIED_BRACKET6:
            tax = BASE_MARRIED6
          else:
            tax = BASE_MARRIED6 + (income - MARRIED_BRACKET6) * TAX_RATE7
      
      print("Tax for %7s filer, with income $%9.2f = $%9.2f"
            %(status, income, tax))
            
main()
