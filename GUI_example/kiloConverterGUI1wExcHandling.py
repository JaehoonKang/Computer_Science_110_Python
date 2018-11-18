import tkinter
#import tkinter.messagebox
import kilotomiles

'''
Converts kilometers to miles
Displays result in dialog box
'''
class KiloConverterGUI:
  # ---------------------------------------------------------------------------
  # Constructor
  def __init__(self):
    # Create instance of MODEL
    self.__kiloVal = kilotomiles.KiloToMiles()

    # Create the main window
    self.__mainWindow = tkinter.Tk()

    #--------------------------------------------------------------------------
    # Frames and widgets

    # Create two frames to group widgets
    self.__topFrame = tkinter.Frame()
    self.__bottomFrame = tkinter.Frame()

    # Create the widgets for the top frame
    self.__kiloEntryLabel = tkinter.Label(self.__topFrame, 
                text='Enter a distance in kilometers: ')
    self.__kiloEntry = tkinter.Entry(self.__topFrame, 
                                     width=10)
    # use bind method to connect <Return> event to callback method
    self.__kiloEntry.bind('<Return>', self.convertFromEntry)

    # Pack top frame widgets
    self.__kiloEntryLabel.pack(side='left')
    self.__kiloEntry.pack(side='left')

    # Create the button widgets for the bottom frame
    self.__convertButton = tkinter.Button(self.__bottomFrame, 
                                          text='Convert', 
                                          command=self.convert)
    self.__quitButton = tkinter.Button(self.__bottomFrame, 
                                       text='Quit', 
                                       command=self.__mainWindow.destroy)
    # Pack the buttons
    self.__convertButton.pack(side='left')
    self.__quitButton.pack(side='left')

    # Pack the frames
    self.__topFrame.pack()
    self.__bottomFrame.pack()


    #--------------------------------------------------------------------------
    # Enter the tkinter main loop
    tkinter.mainloop()

  #----------------------------------------------------------------------------
  # Event Handlers

  # Callback method for entry box
  # Invokes button callback to do work
  def convertFromEntry(self, event):
    self.convert()

  # Callback method for compute button
  # Note use of exception handling instead of validation
  def convert(self):
    try:
      # Get value from kiloEntry widget and set model
      self.__kiloVal.setKilo(float(self.__kiloEntry.get()))

      # Convert and display results in info dialog box
      # Uses 'toString' of self.__kiloVal
      tkinter.messagebox.showinfo('Kilos to Miles', 
                                  str(self.__kiloVal))
    except ValueError as err:
      tkinter.messagebox.showerror('Kilos to Miles', 
                                  "Must provide valid input: %s" % err)
    finally:
      self.__kiloEntry.delete(0, tkinter.END)  # Clear entry box
#----------------------------------------------------------------------------__

# Create instance of KiloConverterGUI class
KiloConverterGUI()
