rainfall = open('rainfall.txt','r')

lines = rainfall.readlines()

new_list = []
new_list_1 = []
while lines:
    #print(lines)

    for i in lines:
      #print(i.strip('\n'))
      new_list.append(i.strip('\n'))
                   
    lines = rainfall.readlines()
#print(new_list)

for x in new_list:
  #print(x.split(' '))
  a = x.split(' ')
  #print(a[1])
  new_list_1.append(a[1])

#print(new_list_1)
print("max: ", max(new_list_1))
print("min: ", min(new_list_1))

SUM = 0
print(new_list_1)
for i in new_list_1:
  SUM += float(i)
  average = SUM / len(new_list_1)
print("average: ", average)
rainfall.close()
