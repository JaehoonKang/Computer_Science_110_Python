import tkinter
#import tkinter.messagebox #No longer needed

'''
Demonstrates Tk class destroy() method when Quit button clicked
as well as info dialog box
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__mainWindow = tkinter.Tk()

    # Create button with 'Click Me!' on face
    # doSomething method executed when clicked
    self.__myButton = tkinter.Button(self.__mainWindow, \
                                    text='Click Me!', \
                                    command=self.doSomething)

    # Create Quit button that executes root widget's destroy() method
    # when clicked
    self.__quitButton = tkinter.Button(self.__mainWindow, \
                                      text='Quit', \
                                      command=self.__mainWindow.destroy)

    # Pack the Buttons
    self.__myButton.pack()
    self.__quitButton.pack()
    
    # Start listener
    tkinter.mainloop()

  # Event handler aka callback function for button   
  def doSomething(self):
    # Display info dialog box
    tkinter.messagebox.showinfo('Response', \
                                'Thanks for clicking the button.')

MyGUI()

