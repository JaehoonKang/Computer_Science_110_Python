'''
Kang Jaehoon & Xuening Wang
C60
Lab12
Vlad
'''

from tkinter import *
from tkinter import messagebox
from counterWP import CounterWP


class CounterGUIWP:
  #--constructor--------------------------------------------------
  def __init__(self):
    self.__main_window = Tk()
    self.__counter = CounterWP() ####
    

    # Create two Controller frames top & mid
    self.__top = Frame(self.__main_window)
    self.__mid = Frame(self.__main_window)
    self.__bottom = Frame(self.__main_window)


    # top frame
    top_button_left = Button(self.__top, text = 'C O U N T  U P ! ',\
                          command = self.count_up)
    top_button_right = Button(self.__top, text = 'C O U N T  D O W N !',\
                             command = self.count_down)
    top_button_left.pack(side = 'left')
    top_button_right.pack(side = 'left')

    mid_button_reset = Button(self.__mid, text = ' RESET Counter ',\
                                 command = self.reset)

    # create static label called prompt in mid frame
    
    self.__prompt = Label(self.__mid, text = 'Set Counter: ')

    self.__entry_box = Entry(self.__mid, width = 7)
    # Bind
    self.__entry_box.bind('<Return>',self.set)

    mid_button_reset.pack(side = 'left')
    self.__prompt.pack(side = 'left')
    self.__entry_box.pack(side = 'left')
    
    
    self.__label = Label(self.__bottom, text = 'Count =  ') 

    # i_val: an IntVar that will hold the current value of the model
    
    self.__i_val = IntVar()

    # invoke set()
    self.__i_val.set

    value = self.__counter
    self.__value = Label(self.__bottom, textvariable = self.__i_val)
    
    self.__label.pack(side = 'left')
    self.__value.pack(side = 'left')

    self.__top.pack()
    self.__mid.pack()
    self.__bottom.pack()

      
    mainloop()
                     

  def count_up (self):
    #self.__entry_box.get_value()
    return self.__counter.increment()
    print(self.__count_up)
  
  def count_down (self):
    return self.__counter.decrement()
    
    
  def reset (self):
    self.__counter.reset()
    

  def set (self,event):
    print(self)
    value = int(self.__entry_box.get())
    #print(value)
    
  def get (self):
    if self.__is_not_negative():
      self.set
      ##print(self.set)
    else:
      self.warn()
    
    
    self.entry_box.delete(0,END) # clear entry box
  
  def __is_not_negative(self):
    return int(self.__counter.get_value()) >= 0

  def __can_decrement(self):
    if self.__is_not_negative():
      self.count_down()
    else:
      self.warn()
               
  def __update_display(self):
    i_val.set(self.__counter.get_value()) 
    
  def warn(self):
    return messagebox.showwarning("Warning","Warning message")


CounterGUIWP()
