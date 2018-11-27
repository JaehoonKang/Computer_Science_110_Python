Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '''
Name: Jaehoon Kang
Email: jkang36@binghamton.edu
Phone: 917-724-6430
Lab Section: C60
Assignment 1
'''
'\nName: Jaehoon Kang\nEmail: jkang36@binghamton.edu\nPhone: 917-724-6430\nLab Section: C60\nAssignment 1\n'
>>> '''
#Analysis

1. Restate the problem: Find the total number of shakes when each person shakes hands with everyone

2. Define the output: The total number of hand shakes

3. Define the input: The total number of people

4. Process: ( n * (n - 1)) / 2
'''
'\n#Analysis\n\n1. Restate the problem: Find the total number of shakes when each person shakes hands with everyone\n\n2. Define the output: The total number of hand shakes\n\n3. Define the input: The total number of people\n\n4. Process: ( n * (n - 1)) / 2\n'
>>> '''
#Analysis

1. Restate the problem: Find the total number of shakes when each person shakes hands with everyone

2. Define the output: The total number of hand shakes. 

3. Define the input: The total number of people: number of people

4. Process: ( n * (n - 1)) / 2
'''
'\n#Analysis\n\n1. Restate the problem: Find the total number of shakes when each person shakes hands with everyone\n\n2. Define the output: The total number of hand shakes. \n\n3. Define the input: The total number of people: number of people\n\n4. Process: ( n * (n - 1)) / 2\n'

>>> def main():
	# In order to get input
	num_ppl = input("input the number of people: ")
	convert_ppl = int(num_people)

	
>>> def main():
	
  # In order to get input
  
  num_ppl = input("Enter the number of people in a room? ")
	
  convert_ppl_num = int(num_ppl)
	
  # Compute output
	
  number_of_people = (convert_ppl_num * (convert_ppl_num -1))/2
	
  # Display the output
	
  print(number_of_people)
	
  main()
