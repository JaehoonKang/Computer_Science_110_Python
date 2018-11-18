import tkinter

'''
Displays two labels with text
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__mainWindow = tkinter.Tk()

    # Create two labels and set their text
    self.__label1 = tkinter.Label(self.__mainWindow, \
                                text='Hello World!')
    self.__label2 = tkinter.Label(self.__mainWindow, \
                     text='This is my GUI program.')

    # Call both Label widgets' pack method    
    self.__label1.pack()
    self.__label2.pack()

    # Start listener
    tkinter.mainloop()

MyGUI()

