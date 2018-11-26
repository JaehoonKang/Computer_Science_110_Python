from tkinter import *
import random



class GuessingGame:

    def __init__(self):
        self.__window = Tk()
        
        self.__upper_frame = Frame(self.__window, width=300, height = 250)
        self.__upper_frame.grid(row=0, column=0)

        self.__lower_frame = Frame(self.__window, width=300, height = 250)
        self.__lower_frame.grid(row=3, column=0)

        self.__label_intro = Label(self.__upper_frame, text="Welcome to the Guessing Game")
        self.__label_intro.grid(row=0, column =0)

        self.__label_right = Label(self.__upper_frame, text="the answer you put is lower")
        self.__label_right.grid(row=1, column =0)

        self.__entry_guess = Entry(self.__lower_frame)
        self.__entry_guess.grid(row=1, column=0)

        self.__button_input = Button(self.__lower_frame, text="enter", fg="white", bg="black")
        self.__button_input.grid(row=1, column=1)

        self.__window.mainloop()

GuessingGame()
