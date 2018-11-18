import tkinter

'''
Creates labels in two different frames
'''
class MyGUI:
  def __init__(self):
    # Create main window
    self.__mainWindow = tkinter.Tk()

    # Create two frames, for top and bottom of window
    self.__topFrame = tkinter.Frame(self.__mainWindow)
    self.__bottomFrame = tkinter.Frame(self.__mainWindow)

    # Create three labels that live in the top frame
    self.__label1 = tkinter.Label(self.__topFrame, \
                                text='Omne')
    self.__label2 = tkinter.Label(self.__topFrame, \
                                text='Trium')
    self.__label3 = tkinter.Label(self.__topFrame, \
                                text='Perfectum')
    
    # Pack the labels into the top frame so they are stacked
    # Note that this is the default behavior
    # (They would do this anyway)
    self.__label1.pack(side='top')
    self.__label2.pack(side='top')
    self.__label3.pack(side='top')
##    self.label1.pack()#side='top')
##    self.label2.pack()#side='top')
##    self.label3.pack()#side='top')

    # Create three labels that live in the bottom frame
    self.__label4 = tkinter.Label(self.__bottomFrame, \
                                text='Omne')
    self.__label5 = tkinter.Label(self.__bottomFrame, \
                                text='Trium')
    self.__label6 = tkinter.Label(self.__bottomFrame, \
                                text='Perfectum')
    
    # Pack the labels into the bottom frame so they are
    # arranged horizontally from left to right
    self.__label4.pack(side='left')
    self.__label5.pack(side='left')
    self.__label6.pack(side='left')
    
    # Then pack the frames into the main window
    self.__topFrame.pack()
    self.__bottomFrame.pack()

    # Start the listener
    tkinter.mainloop()

MyGUI()

