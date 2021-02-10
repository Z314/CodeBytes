# Python program that uses Pythagoras to calculate side lengths of a right angled triangle
# Python version = 3.6
# Author: JP

import tkinter
import math


class pythagoras:

    def __init__(self):
        # main window
        self.main_window = tkinter.Tk()
        
        # create frames
        self.top0_frame = tkinter.Frame(self.main_window)        
        self.top1_frame = tkinter.Frame(self.main_window)
        self.top2_frame = tkinter.Frame(self.main_window)
        self.top3_frame = tkinter.Frame(self.main_window)
        self.top4_frame = tkinter.Frame(self.main_window)
        
        # create the widgets
        self.header = tkinter.Label(self.top0_frame, text='Right Angle Triangle Side Length Calculator')        
        self.length_1_label = tkinter.Label(self.top1_frame, text='Enter First Side Length of Triangle: ')
        self.length_1_entry = tkinter.Entry(self.top1_frame, width=10)
        self.length_2_label = tkinter.Label(self.top2_frame, text='Enter Second Side Length of Triangle: ')
        self.length_2_entry = tkinter.Entry(self.top2_frame, width=10)
        
        self.radio_var_set1 = tkinter.IntVar()
        self.radio_var_set2 = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.top1_frame, text='Side a', variable=self.radio_var_set1, value=1)
        self.rb2 = tkinter.Radiobutton(self.top1_frame, text='Side b', variable=self.radio_var_set1, value=2)
        self.rb3 = tkinter.Radiobutton(self.top1_frame, text='Side c (Hypotenuse)', variable=self.radio_var_set1, value=3)
        self.rb4 = tkinter.Radiobutton(self.top2_frame, text='Side a', variable=self.radio_var_set2, value=4)
        self.rb5 = tkinter.Radiobutton(self.top2_frame, text='Side b', variable=self.radio_var_set2, value=5)
        self.rb6 = tkinter.Radiobutton(self.top2_frame, text='Side c (Hypotenuse)', variable=self.radio_var_set2, value=6)
        
        # Solution placed here
        self.solutionLabel = tkinter.Label(self.top3_frame, text='Third Side Length of Triangle is: ')
        self.ans = tkinter.StringVar()
        self.ans_label = tkinter.Label(self.top3_frame, textvariable=self.ans)
        
        # Button to find solution
        self.button1 = tkinter.Button(self.top4_frame, text='Solve', \
                                             command=self.calculate)
        
        # Pack frames and widgets
        self.header.pack(side='left')
        self.length_1_label.pack(side='left')
        self.length_1_entry.pack(side='left')
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')          

        self.length_2_label.pack(side='left')
        self.length_2_entry.pack(side='left')
        self.rb4.pack(side='left')
        self.rb5.pack(side='left')
        self.rb6.pack(side='left') 
        
        self.solutionLabel.pack(side='left')
        self.ans_label.pack(side='left')
        
        self.button1.pack(side='left')
        self.top0_frame.pack(side='top')       
        self.top1_frame.pack(side='top')
        self.top2_frame.pack(side='top')
        self.top3_frame.pack(side='top')
        self.top4_frame.pack(side='top')
        
        # main loop
        tkinter.mainloop()
        
    def calculate(self):
        # convert user inputs to float
        length_1_entry = float(self.length_1_entry.get())
        length_2_entry = float(self.length_2_entry.get())
        
        rb_set1_selected = self.radio_var_set1.get()
        rb_set2_selected = self.radio_var_set2.get()
        
        if rb_set1_selected == 1 and rb_set2_selected == 5:
            solution = math.sqrt(length_1_entry ** 2 + length_2_entry ** 2)
        elif rb_set1_selected == 1 and rb_set2_selected == 6:
            solution = math.sqrt(length_2_entry ** 2 - length_1_entry ** 2)
        elif rb_set1_selected == 2 and rb_set2_selected == 4:
            solution = math.sqrt(length_1_entry ** 2 + length_2_entry ** 2)
        elif rb_set1_selected == 2 and rb_set2_selected == 6:
            solution = math.sqrt(length_2_entry ** 2 - length_1_entry ** 2)
        elif rb_set1_selected == 3 and rb_set2_selected == 4:
            solution = math.sqrt(length_1_entry ** 2 - length_2_entry ** 2)
        elif rb_set1_selected == 3 and rb_set2_selected == 5:
            solution = math.sqrt(length_1_entry ** 2 - length_2_entry ** 2)
        else: 
            solution = "No Solution"
        
        # convert to string and store in StringVar object
        self.ans.set(solution)

        
# instance of the class
instance1 = pythagoras() 
