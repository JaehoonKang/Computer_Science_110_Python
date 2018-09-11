'''
Name: Jaehoon Kang
Email: jkang36@binghamton.edu
Phone: 917-724-6430
Lab Section: C60
Assignment 1
'''
'''
#Analysis

1. Restate the problem:

  Find the total number of hand shakes when each person shakes in a room hands with everyone

2. Define the output:

  The total number of hand shakes => num_hands

3. Define the input

  The total number of people in case someone inputs a string value => num_ppl_str
  
  Convert num_pple_str to integer value => num_ppl

4. Process: formula: ( num_ppl * (num_ppl - 1)) / 2
'''

# Design

def main():

  #In order to get input
    
  num_ppl_str = input("Enter the number of people in a room: ")

  num_ppl = int(num_ppl_str)

  #Compute output

  num_hands = int((num_ppl * (num_ppl -1)) / 2)

  #Display the output

  print(num_ppl, "people can perfom", num_hands,"handshakes")

main()
