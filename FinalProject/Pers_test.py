from tkinter import *


class GUI:
  global points
  points = 0
  
  def __init__(self):
    self.__window = Tk()

    self.__label = Label(self.__window, text = "Question 1")
    self.__label.grid(columnspan = 3)

    #self.__entry.config("<Return>", self.action)

    self.__button1 = Button(self.__window)
    self.__button1.config(text = "hi", command = self.question_two)
    self.__button1.config(text = "hi", command = self.answer_one)
    self.__button1.grid(row = 1, column = 0)

    self.__button2 = Button(self.__window)
    self.__button2.config(command = self.question_two)
    self.__button2.config(command = self.answer_two)
    self.__button2.grid(row = 1, column = 1)

    self.__button3 = Button(self.__window)
    self.__button3.config(command = self.question_two)
    self.__button3.config(command = self.answer_three)
    self.__button3.grid(row = 1, column = 2)

    self.__button4 = Button(self.__window)
    self.__button4.config(command = self.question_two)
    self.__button4.config(command = self.answer_four)
    self.__button4.grid(row = 1, column = 3)


    self.__window.mainloop()


  def question_two(self):
    self.__label.config(text = "Question 2")


    self.__button1 = Button(self.__window)
    self.__button1.config(text = "Hello", command = self.question_three)
    self.__button1.config(command = self.answer_one)
    self.__button1.grid(row = 1, column = 0)

    self.__button2 = Button(self.__window)
    self.__button2.config(command = self.question_three)
    self.__button2.config(command = self.answer_two)
    self.__button2.grid(row = 1, column = 1)

    self.__button3 = Button(self.__window)
    self.__button3.config(command = self.question_three)
    self.__button3.config(command = self.answer_three)
    self.__button3.grid(row = 1, column = 2)

    self.__button4 = Button(self.__window)
    self.__button4.config(command = self.question_three)
    self.__button4.config(command = self.answer_four)
    self.__button4.grid(row = 1, column = 3)

  def question_three(self):
    self.__label.config(text = "Question 3")


    self.__button1 = Button(self.__window)
    self.__button1.config(command = self.question_four)
    self.__button1.config(command = self.answer_one)
    self.__button1.grid(row = 1, column = 0)

    self.__button2 = Button(self.__window)
    self.__button2.config(command = self.question_four)
    self.__button2.config(command = self.answer_two)
    self.__button2.grid(row = 1, column = 1)

    self.__button3 = Button(self.__window)
    self.__button3.config(command = self.question_four)
    self.__button3.config(command = self.answer_three)
    self.__button3.grid(row = 1, column = 2)

    self.__button4 = Button(self.__window)
    self.__button4.config(command = self.question_four)
    self.__button4.config(command = self.answer_four)
    self.__button4.grid(row = 1, column = 3)

    


    



  def answer_one(self):
    global points
    points += 1
    print(points)

  def answer_two(self):
    global points
    points += 2
    print(points)


  def answer_three(self):
    global points
    points += 3
    print(points)
  def answer_four(self):
    global points
    points += 4
    print(points)

GUI()

