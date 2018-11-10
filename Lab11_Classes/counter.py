'''
Models simple up/down counter that maintains a single count
Methods:
  get_count()
  incrememt()
  decrement()
  set()
  reset()
  'to_string'
'''

## Start your class with the keyword 'class' and the name of the class:
class Counter:  
  #----------------------------------------------------------------------------  
  # Constructor
  ## This method creates the object in a valid state
    
  def __init__(self,init_count = 0):  
    ## Initialize the instance variable that represents the count
    self.__count = init_count 
    
  #----------------------------------------------------------------------------
  # Accessors
  ## return the information about the state of the object

  # return current value of count
  def get_count(self):
    ## Your code here
    return self


  #----------------------------------------------------------------------------
  # Mutators

  def increment(self):
    ## Your code here
    self.__count += 1

  # Does NOT stop at 0
  def decrement(self):
    ## Your code here
    self.__count -= 1
  
  def set_count(self, value):
    ## Your code here
    self.__count = value
    
  def reset(self):
    ## Your code here
    self.__count = 0

  #----------------------------------------------------------------------------
  # 'toString'

  # String representation of object's current state
  def __str__(self):
    return "Count = %d" % (self.__count)## Your code here)
