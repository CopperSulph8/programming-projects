# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style

class MontyHall(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

       
        tk.Tk.wm_title(self, "Monty Hall Problem")
        
        
        window = tk.Frame(self)
        window.pack(side="top", fill="both", expand = True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (WelcomePage, ExplainPage, GraphPage):

            frame = F(window, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class WelcomePage(tk.Frame):
    
    def __init__(self, parent, window):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome Page")
        
        
        label.pack(pady=10,padx=10)
        

        button1 = ttk.Button(self, text="What is the Monty Hall Problem?", command=lambda: window.show_frame(ExplainPage))
        button1.pack()
        
        button2 = ttk.Button(self, text="Graph Page", command=lambda:window.show_frame(GraphPage))
        
        button2.pack()
        
    
class ExplainPage(tk.Frame):
    
    def __init__(self, parent, window):
        
        tk.Frame.__init__(self, parent)
        
        text = tk.Text(self)
        
        text.pack(pady=10,padx=10)
        
        explaination = """
The Monty Hall problem is a counter-intuitive statistics puzzle:

There are 3 doors, behind which are two goats and a car.
You pick a door (call it door A). You're hoping for the car of course.
Monty Hall, the game show host, examines the other doors (B & C),
And opens one with a goat. (If both doors have goats, he picks randomly.)

Here is the game: 
    Do you stick with door A (original guess) or switch to the unopened door? 
    
    Does it matter??
    
    Let's find out on the Graph Page
    
"""
        text.insert(tk.END, explaination)
        
        button = ttk.Button(self, text="Back to Home", command=lambda: window.show_frame(WelcomePage))
        
        button.pack()
        
class GraphPage(tk.Frame):
    
    def __init__(self, parent, window):
        
        tk.Frame.__init__(self, parent)
        
        
        
        def Graph():
            
            style.use('classic')
            
            fig = plt.figure()
            
            plt.xlabel("Number of Iterations")
            
            plt.ylabel("Percentage for Win Ratio (%)")
            
            plt.title("Monty Hall Analysis")
            
            plt.axis([0,1000,0,100])
            
            doors = [1,1,2] # 1 = Goat, 2 = Car
            
            Swin = 1
            
            Sloss = 1
            
            Cwin = 1
            
            Closs = 1
            
            n = 1000
            
            changeGraph = []
            
            stickGraph = []
            
            for i in range(n):
                
                
                
                firstPlayerChoice = random.randint(0,2)
                
                goatRand = random.randint(0,1)
                
                secondPlayerChoice = random.randint(0,1) # 0 = Stick, 1 = Change
                
                if secondPlayerChoice == 0:
                    
                    if doors[firstPlayerChoice] == 1:
                        
                        Sloss += 1
                
                    else:
                        
                        Swin += 1
                else:
                    
                    if doors[firstPlayerChoice] == 2:
                        
                        Closs += 1
                        
                    else:
                        
                        Cwin += 1
                        
                 
                
                stickGraph.append(Swin/(Swin+Sloss)*100)
                 
                
                changeGraph.append(Cwin/(Cwin+Closs)*100)        
                
                
            plt.plot(stickGraph, label="Stick")
            
            plt.plot(changeGraph, label="Change")
            
            plt.legend()
            
            plt.show()
            
            
        
        button1 = ttk.Button(self, text="Display Graph", command=Graph)
    
        button1.pack()
        
        
        button2 = ttk.Button(self, text="Back to Home", command=lambda: window.show_frame(WelcomePage))
        
        button2.pack()
        
        
        
        
Initialise = MontyHall()

Initialise.mainloop()
