outfile = open("temp_conv.txt", "w")

for temp_in_fahrenheit in range(-300, 213):
  temp_in_celsius = 5 / 9  * (temp_in_fahrenheit - 32)

  #print("%10d   %10.2f" %(temp_in_fahrenheit, temp_in_celsius))
  #data = str(temp_in_fahrenheit)+ ' ' + str(temp_in_celsius)
  outfile.write("%10d %10.2f\n" %(temp_in_fahrenheit, temp_in_celsius))

outfile.close()
