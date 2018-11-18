'''
Rose Williams
rosew@binghamton.edu
GUI and MVC example
'''

'''
Virtual counter GUI
Allows user to count up or down using buttons, reset counter using button,
   and set counter by entering value and pressing <Enter> on keyboard
Output:
   value of counter displayed in Label (int)
Input:
   value of counter entered into Entry box (int)
Tasks:
  Create GUI with
    Model -
      counter (Counter)
    Controllers -
      buttonUp, buttonDown, buttonReset (Button)
      entry (Entry)
    View -
      value (Label)
  countUp()
  countDown()
  reset()
  set()
'''

from tkinter import *        #All classes in GUI module
from Counter import Counter  #Model class

# Provides GUI representation (View and Controller) of counter (Model)
class CounterGUI:
  # --------------------------------------------------------------------------
  # Constructor

  # Creates instance of Model class (Counter), creates, configures, and
  # places all Controller and View widgets, and starts listener
  def __init__(self):
    # Create main window
    self.__win = Tk()

    # Create Controller frames
    self.__top = Frame(self.__win)
    self.__mid = Frame(self.__win)
    
    # Create View frame
    self.__bottom = Frame(self.__win)
    
    # Create Model
    self.__counter = Counter()

    # Create, configure, and place Up/Down button controls in top frame(part of Controller)
    # Clicking Up button will invoke countUp() method
    self.__buttonUp = Button(self.__top, text = "C O U N T   U P !", command = self.countUp)
    self.__buttonUp.pack(side = 'left')
    # Clicking Down button will invoke countDown() method
    self.__buttonDown = Button(self.__top, text = "C O U N T   D O W N !", command = self.countDown)
    self.__buttonDown.pack(side = 'right')

    # Create, configure, and place Reset button control in middle frame (part of Controller)
    # Clicking Reset button will invoke reset() method
    self.__buttonReset = Button(self.__mid, text = " RESET Counter ", command = self.reset)
    # Create, configure, and place prompt and entry box control in middle frame (part of Controller)
    # Typing a value in entry box and pressing <Enter> on the keyboard will invoke set() method
    self.__prompt = Label(self.__mid, text = 'Set Counter: ')
    self.__entry = Entry(self.__mid, width = 7)
    self.__entry.bind('<Return>', self.set)

    self.__buttonReset.pack(side = 'left')
    self.__prompt.pack(side = 'left')
    self.__entry.pack(side = 'left')

    # Create, configure, and place IntVar and labels to display Model data in bottom frame (part of View)
    # Label output
    self.__label = Label(self.__bottom, text = 'Count = ')
    # Create IntVar to hold string representation of current value of counter
    self.__iVal = IntVar()
    self.__iVal.set(self.__counter.getValue())
    # Create label to display IntVar
    self.__value = Label(self.__bottom, textvariable = self.__iVal)

    self.__label.pack(side = 'left')
    self.__value.pack(side = 'right')

    # Place frames vertically from top to bottom
    self.__top.pack()
    self.__mid.pack()
    self.__bottom.pack()

    # Enter the Tkinter main loop
    mainloop()
  
  # countUp() - causes counter to be incremented and modifies StringVar (View) accordingly (mutator)
  def countUp(self):
    self.__counter.increment() # Note that the model takes care of its own state, here it is incrementing
    self.__iVal.set(self.__counter.getValue()) # Get the new value from the model and display it

  # countDown() - causes counter to be decremented and modifies StringVar (View) accordingly (mutator)
  def countDown(self):
    self.__counter.decrement() # Note that the model takes care of its own state, here it is decrementing
    self.__iVal.set(self.__counter.getValue()) # Get the new value from the model and display it

  # reset() - causes counter to be re-initialized and modifies StringVar (View) accordingly (mutator)
  def reset(self):
    self.__counter.reset() # Note that the model takes care of its own state, here it is re-initializing its state
    self.__iVal.set(self.__counter.getValue()) # Get the new value from the model and display it

  # set() - causes counter to be set to value entered into entry box and modifies IntVar (View) accordingly (mutator)
  # param: event - produced when user presses <Enter>
  def set(self, event):
    newValue = int (self.__entry.get()) # Get value that was entered into entry box
    # Note that newValue is NOT named self.__newValue because it is a local variable, NOT an instance variable
    # ONLY instance variables (which must be initialized in the constructor) are to use the self.__<variableName> naming convention
    self.__counter.set(newValue)  # Have the model use the value to modify itself
    self.__iVal.set(self.__counter.getValue()) # Get the new value from the model and display it
    self.__entry.delete(0, END)  # Clear entry box
    
# Create a CounterGUI object
CounterGUI()
