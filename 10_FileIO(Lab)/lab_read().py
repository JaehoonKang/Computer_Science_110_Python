rainfall = open('rainfall.txt','r')
new_list = []
line = rainfall.read()

while line:
  values = line.split()
  line = rainfall.read()


  for i in range(1,len(values),2):
    num = float(values[i])
    new_list.append(num)
  
  print(max(new_list))
  print(min(new_list))

SUM = 0
for i in new_list:
  SUM += i
  average = SUM / len(new_list)
print(average)
rainfall.close()
