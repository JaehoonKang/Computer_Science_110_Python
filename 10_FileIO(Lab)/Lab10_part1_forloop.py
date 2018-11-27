# a program that computes and displays the minimum, maxmum and average rainfall
# processing the data in a file named rainfall.txt
rainfall = open('rainfall.txt','r')
# Iterating over the file with a for loop
new_list=[]
for line in rainfall:
  values = line.split()
  #print(type(values))
  #print(values[1])
  new_list.append(float(values[1]))
  #number = values[1]
  #print(number)
#print(new_list)

print(max(new_list))
print(min(new_list))

SUM = 0
for i in new_list:
  SUM += i
  average = SUM / len(new_list)
print(average)

# using the readline() method

