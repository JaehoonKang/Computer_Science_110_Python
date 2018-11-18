from tkinter import * 

'''
Demonstrates entry box
'''
class sampleGUI:   
  # constructor
  def __init__(self):
    # Create GUI window and set its titlebar
    self.__win = Tk()
    self.__win.title ('Entry Box')

    # Create label, initialize its text, and place in window
    self.__label = Label(self.__win, text = 'This is a label.')
    self.__label.pack()

    # Create entry box, bind it to key event,
    # register it with event handler, and place in window 
    self.__entry = Entry(self.__win)
    # use bind method to connect <Return> event to callback method
    self.__entry.bind('<Return>', self.changeColor)
    self.__entry.pack()

    #create and label button, register its event handler, and place in window  
    self.__button = Button(self.__win, text = 'This is a button.')
    # use config method to set button's command option to event handler
    self.__button.config(command = self.action)
    self.__button.pack()

    #Start listener
    self.__win.mainloop()

  # ---------------------------------------------------------------------------
  # Event Handlers

  # callback method (i.e., event handler) invoked when button is pressed
  # Note that event parameter is not required in this context
  def action(self):
    self.__label.config(text = 'The button was pressed.')

  # callback method invoked when <Enter> pressed inside entry box
  # NOTE – EVENT PARAMETER is required, but use is optional
  def changeColor(self, event):
    newColor = self.__entry.get()
    self.__button.config(bg = newColor)
    self.__entry.delete(0, END)  # Clear entry box

sampleGUI()
