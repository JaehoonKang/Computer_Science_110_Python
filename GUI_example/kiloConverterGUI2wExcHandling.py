import tkinter
import kilotomiles

'''
Converts kilometers to miles
Displays result in Label
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

    # Create three frames to group widgets
    self.__topFrame = tkinter.Frame()
    self.__midFrame = tkinter.Frame()
    self.__bottomFrame = tkinter.Frame()

    # Create top frame widgets
    self.__kiloEntryLabel = tkinter.Label(self.__topFrame, 
                text='Enter distance in kilometers: ')
    self.__kiloEntry = tkinter.Entry(self.__topFrame,
                                     width = 10)

    # use bind method to connect <Return> event to callback method
    self.__kiloEntry.bind('<Return>', self.convertFromEntry)

    # Pack top frame widgets
    self.__kiloEntryLabel.pack(side='left')
    self.__kiloEntry.pack(side='left')

    # Create middle frame widgets
    # Associate StringVar with label for output
    # Use set method to initialize    
    self.__value1 = tkinter.StringVar()
    self.__value1.set("%.2f kilometers" % self.__kiloVal.getKilo())

    # Create label and associate with StringVar
    # Value stored in StringVar will be
    #  automatically displayed in label
    self.__kiloLabel = tkinter.Label(self.__midFrame,
                                     textvariable = self.__value1)
    self.__middleLabel = tkinter.Label(self.__midFrame, 
                                       text=' converted to miles = ')
    
    # Associate StringVar with label for output
    # Use set method to initialize
    self.__value2 = tkinter.StringVar()
    self.__value2.set("%.2f miles" % self.__kiloVal.toMiles())

    # Create label and associate with StringVar
    # Value stored in StringVar will be
    #  automatically displayed in label
    self.__milesLabel = tkinter.Label(self.__midFrame, 
                                textvariable=self.__value2)

    # Pack middle frame widgets
    self.__kiloLabel.pack(side='left')
    self.__middleLabel.pack(side='left')
    self.__milesLabel.pack(side='left')

    # Create bottom frame button widgets
    self.__convertButton = tkinter.Button(self.__bottomFrame, 
                                 text='Convert', 
                                 command=self.convert)
    self.__quitButton = tkinter.Button(self.__bottomFrame, 
                            text='Quit', 
                            command=self.__mainWindow.destroy)

    # Pack buttons
    self.__convertButton.pack(side='left')
    self.__quitButton.pack(side='left')

    # Pack frames
    self.__topFrame.pack()
    self.__midFrame.pack()
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

      #
      self.__value1.set("%.2f kilometers" % self.__kiloVal.getKilo())

      # Convert kilometers to miles and 
      # store formatted result in StringVar object
      # Wll automatically update milesLabel widget
      self.__value2.set("%.2f miles" % self.__kiloVal.toMiles())
      
    # Entry box input was inappropriate
    except ValueError as err:
      tkinter.messagebox.showerror('Kilos to Miles', 
                                  "Must provide valid input: %s" % err)
      self.__kiloVal.resetKilo()
      self.__value1.set("%.2f kilometers" % self.__kiloVal.getKilo())
      self.__value2.set("%.2f miles" % self.__kiloVal.toMiles())
    finally:
      self.__kiloEntry.delete(0, tkinter.END)  # Clear entry box

# Create instance of KiloConverterGUI class
KiloConverterGUI()
