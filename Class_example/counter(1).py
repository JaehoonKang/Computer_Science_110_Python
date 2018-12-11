
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

class Counter:
  #----------------------------------------------------------------------------  
  # Constructor
  
  def __init__(self, init_count = 0):  
    self.__count = init_count

  #----------------------------------------------------------------------------
  # Accessors

  # return current value of count
  def get_count(self):  
    return self.__count

  #----------------------------------------------------------------------------
  # Mutators

  def increment(self):
    self.__count += 1

  # Does NOT stop at 0
  def decrement(self):
    self.__count -= 1
    
  #param value(int) - used to set count
  def set_count(self, value):
    self.__count = value
    
  def reset(self):
    self.__count = 0

  #----------------------------------------------------------------------------
  # 'to_string'

  # String representation of object's current state
  def __str__(self):
    return "Count = %d" % (self.__count)

