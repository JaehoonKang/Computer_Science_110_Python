'''
Rose Williams
'''

'''
This program finds the population of a city via database query
Output:
  query result (str)
Input:
  city (str)
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Missing Argument'
    self.__message = 'City is blank or contains invalid characters'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def get_title(self):
    return self.__title
    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDBPopRange:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, db_name):
    conn = sqlite3.connect(db_name)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
    #self.__current_city = ""
    self.__max_population = ""
    self.__min_population = ""
    self.__answer = None

# -- Predicate ---------------------------------------------------------------

  def __is_valid_range(self, a, b):
    return a.isdigit() and b.isdigit() and int(a) <= int(b) 

# -- Accessor-----------------------------------------------------------------

  def get_answer(self):
    return self.__answer
  
# -- Mutators ----------------------------------------------------------------

  # 
  # param city_name (str)
  #def set_city(self, city_name):
    #self.__current_city = city_name

  def set_pop(self, minPop, maxPop):
    self.__min_population = minPop
    self.__max_population = maxPop


  # raises BadArgument Exception if city is blank or contains invalid chars
  def pop_query(self):
    
    if self.__is_valid_range(self.__min_population, self.__max_population):
      self.__cursor.execute('select name,population from city where population >= ? and population <= ? order by population',\
      (self.__min_population,self.__max_population))
    else:
      raise BadArgument()


  # Close connection to db
  def close_connection(self):
    self.__cursor.close()

# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that if city isn't in database, then answer will be None
    # If city is in database, answer will be a tuple object
    # Will have to get element[0] of tuple in order to use it
    #answer = self.__cursor.fetchone()

    # Note that 4th format specifier denotes a string rather than an int in 
    # order to accommodate possibility that answer is None
    #return '%s %s %s %s\n' % (
      #('The population of' if answer else 'There is no city named'),
      #self.__current_city,
      #('is' if answer else 'in the database'),
      #('' if answer == None else str(answer[0])) )
    self.__list_of_cities = self.__cursor.fetchall()
    string = ""
    if self.__list_of_cities:
      for element in self.__list_of_cities:
        string += element[0] +" has a Population of : "\
        +str(element[1]) +"\n"
    else:
      string = "There are no cities in that range"
    return string
  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
  
# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
def main():
  # set up connection and create cursor
  query = QueryWorldDBPopRange('worldDB')
  #query = QueryWorldDB('world.db')

  # get input from user (priming read)
  #city = input("Find the population of a city\nEnter the city name, " + \
               #"separate multi-word cities by '_'\n" + \
               #"(Press <Enter> to quit):  ")
  
  # let user get as many results as desired
  #while city:
    #try:
      # set up and issue query
      #query.set_city(city.strip())
      #query.pop_query()
      # show results
      #print(query)
    #except BadArgument as err:
      # city input empty or malformed
      #print('\n%s: %s\n' % (err.get_title(), str(err) ))
       
    # let user enter another city (continuation read)
    #city = input("Find the population of a city\nEnter the city name, " + \
                 #"separate multi-word cities by '_'\n" + \
                 #"(Press <Enter> to quit):  ")
  print("Find the vity by population \n")

  # get input from user (priming read)
  populationMin = input("Enter the min population, "+\
               "(Press <Enter> to quit):  ")

  populationMax = input("Enter the max population, "+\
               "(Press <Enter> to quit):  ")

  # let user get as many results as desired
  while populationMin and populationMax:
    try:
      # set up and issue query
      query.set_pop(populationMin,populationMax)
      query.pop_query()
      # show results
      print(query)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.getTitle(), str(err) ))

    # let user enter another city (continuation read)
    print("Find the City by population \n")

    # get input from user (priming read)
    populationMin = input("Enter the min population, "+\
                 "(Press <Enter> to quit):  ")

    populationMax = input("Enter the max population, "+\
                 "(Press <Enter> to quit):  ")
  
  # close connection to db
  query.close_connection()

main()
                            
                            
                    
