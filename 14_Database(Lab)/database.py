import sqlite3
conn = sqlite3.connect('worldDB')
cursor = conn.cursor( )

cursor.execute("select * from sqlite_master;")
tableInfo = cursor.fetchall()

#for data in tableInfo:
	#print(data)


cursor.execute("pragma table_info('city')")
fieldList = cursor.fetchall()


cityName = "Mumbai"
cursor.execute("select population from city where name = ?", (cityName,))
print("Question1: ", cursor.fetchone())
#Q1. 10500000


#for field in fieldList:
	#print(field[1])

#cursor.execute("select name from city where population > 5000000")

#Q2. São_Paulo, Rio_de_Janeiro, London, Cairo, Jakarta, Mumbai, Delhi, Teheran, Tokyo, Shanghai, Peking, Chongqing, Tianjin, Santafé_de_Bogotá, Kinshasa, Seoul
#Ciudad_de_México, Karachi, Lahore, Lima, Bangkok, Istanbul, Moscow, New_York

#print (cursor.fetchone())


#cursor.execute("select name from city where population > 4000000")
#cities = cursor.fetchall()

#for city in cities:
  #print(city)
#print (cursor.fetchone())
#print (cursor.fetchone())


cursor.execute("select name from city where population > 4000000 and population < 5000000 order by name")
cities = cursor.fetchall()

#for city in cities:
	#print(city[0])
#Q3. Baghdad, Calcutta, Harbin, Kanton, Santiago_de_Chile, Shenyang, Singapore, St_Petersburg, Wuhan





#Q4.

cursor.execute("select name from city where population < 5000000 and population > 4000000 order by population")
cities = cursor.fetchall()
#print(cities)
cities.reverse()
#print()

for city in cities:
  cursor.execute("select population from city where name = ?", (city))
  print("Question4:", city, ":", cursor.fetchone())

  

