import tkinter
import tkinter.messagebox

'''
Demonstrates a group of Checkbutton widgets
'''
class MyGUI:
  # Constructor
  def __init__(self):
    # Create main window
    self.mainWindow = tkinter.Tk()

    # Create two frames:  One for checkbuttons
    # and another for regular Button widgets
    self.topFrame = tkinter.Frame(self.mainWindow)
    self.bottomFrame = tkinter.Frame(self.mainWindow)
    
    # Create three IntVar objects to use with
    # Checkbuttons
    self.cbVar1 = tkinter.IntVar()
    self.cbVar2 = tkinter.IntVar()
    self.cbVar3 = tkinter.IntVar()
    
    # Initialize intVars to 0 (unselected)
    # Note: must use set() method (NOT =)
    self.cbVar1.set(0)
    self.cbVar2.set(0)
    self.cbVar3.set(0)
    
    # Create Checkbutton widgets in topFrame
    self.cb1 = tkinter.Checkbutton(self.topFrame, \
               text='Option 1', variable=self.cbVar1)
    self.cb2 = tkinter.Checkbutton(self.topFrame, \
               text='Option 2', variable=self.cbVar2)
    self.cb3 = tkinter.Checkbutton(self.topFrame, \
               text='Option 3', variable=self.cbVar3)

    # Pack Checkbuttons
    self.cb1.pack()
    self.cb2.pack()
    self.cb3.pack()

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
    
    # Start mainloop
    tkinter.mainloop()


  # ---------------------------------------------------------------------------
  # Event Handlers

  # Callback function that is invoked when OK button is clicked   
  def showChoice(self):
    # Create message string
    self.message = 'You selected:\n'

    # Determine which Checkbuttons are selected and
    # build message string accordingly
    if self.cbVar1.get() == 1:
        self.message = self.message + '1\n'
    if self.cbVar2.get() == 1:
        self.message = self.message + '2\n'
    if self.cbVar3.get() == 1:
        self.message = self.message + '3\n'

    # Display message in info dialog box.
    tkinter.messagebox.showinfo('Selection', self.message)

# Create instance of the MyGUI class
MyGUI()
