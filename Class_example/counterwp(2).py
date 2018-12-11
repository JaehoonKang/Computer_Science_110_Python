'''
The CounterWP class models a simple up/down counter that maintains a single value
The encapsulated value is NOT permitted to go below 0
'''
class CounterWP:
  # Constructor
  def __init__(self):
    self.__count = 0

  #----------------------------------------------------------------------------
  # Predicates

  # return false when 0, true otherwise
  def is_ok_to_decrement(self):
    return self.__count > 0

  #----------------------------------------------------------------------------
  # Accessors

  # get_count() - returns copy of __count instance variable (accessor)
  # return:  current count of __count
  def get_count(self):
    return self.__count

  #----------------------------------------------------------------------------
  # Mutators

  def increment(self):
    self.__count += 1

  # Does NOT stop at 0
  def decrement(self):
    if self.is_ok_to_decrement():
      self.__count -= 1
  
  def reset(self):
    self.__count = 0
  
  #----------------------------------------------------------------------------
  # 'to_string'

  # String representation of object's current state
  def __str__(self):
    return "Count = %d" % (self.__count)
    

def main():
  counter = CounterWP()
  for up_click in range(10):
    counter.increment()
  print(counter)
  print("----------")
  for down_click in range(10):  
    counter.decrement()
  print(counter)
  print("----------")
  for down_click in range(10):
    counter.decrement()
    print(counter)
  print("----------")
  counter.reset()
  for up_click in range(10):
    counter.increment()  
  print(counter)

main()
  
  
