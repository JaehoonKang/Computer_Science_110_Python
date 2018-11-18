import tkinter
import kilotomiles

# Converts kilometers to miles
# Displays result in label
# Demonstrates Entry Box without event,
# Model-View-Controller
class KiloConverterGUI:
  def __init__(self):

    # Create model, default state
    self.__model = kilotomiles.KiloToMiles()
    
    # Create the main window
    self.__mainWindow = tkinter.Tk()

    # Create three frames to group widgets
    self.__topFrame = tkinter.Frame(self.__mainWindow) # Controller
    self.__midFrame = tkinter.Frame(self.__mainWindow) # View
    self.__bottomFrame = tkinter.Frame(self.__mainWindow) #Controller

    # Create label and control for the top frame
    self.__promptLabel = tkinter.Label(self.__topFrame, \
                text='Enter a distance in kilometers:')
    self.__kiloEntry = tkinter.Entry(self.__topFrame, \
                                    width=10)

    # Pack top frame's widgets
    self.__promptLabel.pack(side='left')
    self.__kiloEntry.pack(side='left')

    # Create View for the middle frame
    self.__descrLabel = tkinter.Label(self.__midFrame, \
                             text='Converted to miles:')
    
    # Associate StringVar object with an output label
    # The set method can be used to
    # to store a string of blank characters
    self.__value = tkinter.StringVar()
    self.__value.set("%.2f" % 0)
    #self.__value = tkinter.DoubleVar()
    #self.__value.set(0.0)

    # Create label and associate it with StringVar object
    # Any value stored in the StringVar object 
    # will automatically be displayed in the label
    self.__milesLabel = tkinter.Label(self.__midFrame, \
                                textvariable=self.__value)

    # Pack middle frame's widgets
    self.__descrLabel.pack(side='left')
    self.__milesLabel.pack(side='left')

    # Create button controls for bottom frame
    self.__calcButton = tkinter.Button(self.__bottomFrame, \
                                 text='Convert', \
                                 command=self.convert)
    self.__quitButton = tkinter.Button(self.__bottomFrame, \
                            text='Quit', \
                            command=self.__mainWindow.destroy)

    # Pack buttons
    self.__calcButton.pack(side='left')
    self.__quitButton.pack(side='left')

    # Pack frames
    self.__topFrame.pack()
    self.__midFrame.pack()
    self.__bottomFrame.pack()

    # Start listener
    tkinter.mainloop()

  # ---------------------------------------------------------------------------
  # Event Handlers
  
  # Callback function for Convert button  
  def convert(self):
    # Set model value to value in entry box
    self.__model.setKilo(float(self.__kiloEntry.get()))
                         
    # Convert miles to a string and store it
    # in the StringVar object
    # This will automatically
    # update the milesLabel widget
    self.__value.set("%.2f" % self.__model.toMiles())
    self.__kiloEntry.delete(0, tkinter.END)  # Clear entry box

KiloConverterGUI()
