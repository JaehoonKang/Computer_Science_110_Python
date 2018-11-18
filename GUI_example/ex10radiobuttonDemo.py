import tkinter
import tkinter.messagebox

'''
Demonstrates a group of Radiobutton widgets
'''
class MyGUI:
  # Constructor
  def __init__(self):
    # Create main window
    self.mainWindow = tkinter.Tk()

    # Create two frames. One for Radiobuttons
    # Another for regular Button widgets
    self.topFrame = tkinter.Frame(self.mainWindow)
    self.bottomFrame = tkinter.Frame(self.mainWindow)
    
    # Create IntVar object to use with Radiobuttons
    self.radioVar = tkinter.IntVar()
    
    # Set intVar to 1
    # Note that set() method must be used (NOT =)
    self.radioVar.set(1)

    # Create Radiobutton widgets in topFrame
    self.rb1 = tkinter.Radiobutton(self.topFrame, \
               text='Option 1', variable=self.radioVar, \
               value=1)
    self.rb2 = tkinter.Radiobutton(self.topFrame, \
               text='Option 2', variable=self.radioVar, \
               value=2)
    self.rb3 = tkinter.Radiobutton(self.topFrame, \
               text='Option 3', variable=self.radioVar, \
               value=3)

    # Pack Radiobuttons
    self.rb1.pack()
    self.rb2.pack()
    self.rb3.pack()

    # Create OK button and Quit button
    self.okButton = tkinter.Button(self.bottomFrame, \
                    text='OK', command=self.showChoice)
    self.quitButton = tkinter.Button(self.bottomFrame, \
                      text='Quit', command=self.mainWindow.destroy)

    # Pack Buttons
    self.okButton.pack(side='left')
    self.quitButton.pack(side='left')

    # Pack frames
    self.topFrame.pack()
    self.bottomFrame.pack()
    
    # Start the mainloop
    tkinter.mainloop()

  # Callback method invoked when OK button is clicked
  def showChoice(self):
      tkinter.messagebox.showinfo('Selection', 'You selected option ' +\
                            str(self.radioVar.get()))

# Create instance of MyGUI class
MyGUI()
