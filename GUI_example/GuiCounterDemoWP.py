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
  __watch(): prevents counter from going negative
'''

from tkinter import *        
from CounterWP import CounterWP  #Model

class CounterGUIWP:

  # --------------------------------------------------------------------------
  # Constructor

  # Creates instance of Model class (CounterWP), creates, configures, and 
  # places all of the Controller and View widgets, starts listener
  def __init__(self):
    # Create main window
    self.__win = Tk()

    # Create Controller frames
    self.__top = Frame(self.__win)
    self.__mid = Frame(self.__win)
    
    # Create View frame
    self.__bottom = Frame(self.__win)
    
    # Create Model
    self.__counter = CounterWP()

    # Create, configure, and place Up/Down button controls in top frame
    #(part of Controller)
    # Clicking Up button invokes countUp() event handler
    self.__buttonUp = Button(self.__top, text = "C O U N T   U P !",
                      command = self.countUp)
    self.__buttonUp.pack(side = 'left')
    # Clicking Down button invokes countDown() event handler
    self.__buttonDown = Button(self.__top, text = "C O U N T   D O W N !",
                        command = self.countDown)
    self.__buttonDown.pack(side = 'right')

    # Create, configure, and place Reset button control in middle frame
    # (part of Controller)
    # Clicking Reset button will invoke reset() event handler
    self.__buttonReset = Button(self.__mid, text = " RESET Counter ", 
                         command = self.reset)
    # Create, configure, and place prompt and entry box control in middle frame
    # (part of Controller)
    # Typing value in entry box and pressing <Enter> will invoke set()
    # event handler
    self.__prompt = Label(self.__mid, text = 'Set Counter: ')
    self.__entry = Entry(self.__mid, width = 7)
    self.__entry.bind('<Return>', self.set)

    self.__buttonReset.pack(side = 'left')
    self.__prompt.pack(side = 'left')
    self.__entry.pack(side = 'left')

    # Create, configure, and place IntVar and labels to display Model data
    # on label in bottom frame (part of View)
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

    # Start listener
    mainloop()

  # ---------------------------------------------------------------------------
  # Event handlers
  
  # Increments counter, modifies StringVar (View) accordingly
  def countUp(self):
    self.__counter.increment() # Model takes care of its own state
    self.__iVal.set(self.__counter.getValue()) # Get and display value

  # Decrements counter, modifies StringVar (View) accordingly
  def countDown(self):
    oldVal = self.__counter.getValue()
    self.__counter.decrement() # Model takes care of its own state
    self.__watch(oldVal) # Don't allow negative values
    self.__iVal.set(self.__counter.getValue()) # Get and display value

  # Resets counter, modifies StringVar (View) accordingly
  def reset(self):
    self.__counter.reset() # Model takes care of its own state
    self.__iVal.set(self.__counter.getValue()) # Get and display value

  # Sets value of counter to that entered into entry box,
  # modifies IntVar (View) accordingly 
  # param event created when user presses <Enter>
  def set(self, event):
    oldValue = self.__counter.getValue()
    newValue = int (self.__entry.get()) # Get value entered into entry box
    # Note that above variables are local, NOT instance variables
    self.__counter.set(newValue)  # Have model use value to modify itself
    self.__watch(oldValue) # Don't allow negative values
    self.__iVal.set(self.__counter.getValue()) # Get and display value
    self.__entry.delete(0, END)  # Clear entry box


  # ---------------------------------------------------------------------------
  # Private helper method

  # param oldVal - previous value of counter
  def __watch(self, oldVal):
    if self.__counter.isNegative():
      messagebox.showinfo("Warning: ", "Counter can not become Negative!!")
      self.__counter.set(oldVal)          
    
CounterGUIWP()
