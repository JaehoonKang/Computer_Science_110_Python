'''
Name
email
Lab section and CA name
Lab or Assignment#, Exercise# if applicable
'''

'''
This class represents a patron
A Patron has a name, a status and zero or more books checked out
'''

class Patron:

  # Class Variables ----------------------------------------------------------

  # Maximum number of books Patron can take out (int)
  MAX_BOOKS_OUT = 3

  # Current status of this Patron (str)
  # Will be combined with name of Patron
  STATUS = [" can borrow up to 3 books", " can borrow two more books", \
            " can borrow one more book", " must return book(s)"]


  # Constructor --------------------------------------------------------------

  # params:  name - name of Patron(str)
  # initialize:  self.__name (str), to parameter name,
  #              self.__numBooksOut (int) to 0, and self.__status() (str)
  #                to STATUS[0]
  def __init__(self, name):
    # your code here

  # Predicates ---------------------------------------------------------------

  # True if less then max books checked out, False otherwise
  def canCheckOutBooks(self):
    # your code here

  # True if books checked out, False otherwise
  def hasCheckedOutBooks(self):
    # your code here


  # Accessors ----------------------------------------------------------------

  # returns: name (str)
  def getName(self):
    # your code here
    
  # returns: status (str)
  def getStatus(self):
    # your code here
    
  # returns: number of books out (int)
  def getNumBooksOut(self):
    # your code here

  # Mutators -----------------------------------------------------------------

  # set to STATUS indexed by number of books out
  def __updateStatus(self):
    # your code here
    
  # invokes: updateStatus()
  def increment(self):
    # your code here
    
  # invokes updateStatus()
  def decrement(self):
    # your code here

  # Comparators --------------------------------------------------------------

  # Already written for you:
  # You will need to include these in order to sort Patron objects

  # Shows how two Patrons can be compared with respect to the < relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when they are not the same Patron and other is a Patron
  #          object and name of this Patron is lexicographically less than 
  #          name of other Patron, False otherwise (bool)
  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__name < other.__name

  # Shows how two Patrons can be compared with respect to the == relationship
  # params:  other - another Patron object
  # invokes: type()
  # returns: True when both are same Patron OR both are Patron objects AND
  #          all attributes are equal, False otherwise (bool)
  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and \
            self.__name == other.__name and \
            self.__status == other.__status and \
            self.__numBooksOut == other.__numBooksOut)

  # Convert to str -----------------------------------------------------------

  def __str__(self):
    # your code here
