'''
Name: Xuening Wang
Email: xwang206@binghamton.edu
Phone: 5163616640
Section: C60
CA: Vlad Malcevic
Lab 10
'''

# a program that computes and displays the minimum, maxmum and average rainfall
# processing the data in a file named rainfall.txt
rainfall = open('rainfall.txt','r')

new_list = []
line = rainfall.readline()
while line:
  values = line.split()
  line = rainfall.readline()
  new_list.append(float(values[1]))

print(max(new_list))
print(min(new_list))

SUM = 0
for i in new_list:
  SUM += i
  average = SUM / len(new_list)
print(average)
rainfall.close()


