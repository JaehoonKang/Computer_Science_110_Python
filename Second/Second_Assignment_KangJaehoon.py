'''
Kang Jaehoon
jkang36@binghamton.edu
917-724-6430
C60
'''

'''Anyalsis
Restate the problem

  Ask a user for the number of sides in a polygon he/she wants to create
  
  and compute the number of diagonals inside the polygon

Output to monitor

  number_diagonal (int) - the number of diagonals in a polygon

Input from keyboard

  numb_side (int) = input("how many sides(lines) do you want to have: ")
  
Givens
    
    
Processing

  number_side = n
  
  formula = { n * (n - 1) / 2 } - n

  simplified formula = (n * (n-3))/2

'''

# Design

def main():

  # Define a problem

  print("Computes the number of diagonals in a polygon given the sides")
  
  print("")

  # in order to get input

  num_side_str = input("Enter how many sides you want to have: ")

  num_side = int(num_side_str)

  # Compute output

  num_diagonal = int(((num_side * (num_side - 1)) / 2) - num_side)

  # Display the output

  print("A %d -sided polygon has %d diagonals ==  %d diagonals" %(num_side, num_diagonal, num_diagonal))

main()
