import math
import tkinter as tk
from tkinter.simpledialog import askstring

Windows = tk.Tk()
Windows.title("Circle Calculator")
pi = math.pi
Diameter = float(askstring("Diameter", "Enter diameter "))
Radius = Diameter/2 or float(askstring("Radius", "Enter Radius "))
Diameter = Radius * 2
Circumference = 2*pi * \
    Radius or float(askstring("Circumference", "Enter Circumfernce "))
Area = pi*(Radius**2) or float(askstring("Area", "What is the Area"))


Diameter_Ans = tk.Label(text=f"Diameter is {Diameter}")
Radius_Ans = tk.Label(text=f"Radius is {Radius}")
Circumference_Ans = tk.Label(text=f"Circumference is {Circumference}")
Area_Ans = tk.Label(text=f"Area is {Area}")

Diameter_Ans.pack()
Radius_Ans.pack()
Circumference_Ans.pack()
Area_Ans.pack()
Windows.mainloop()

"""
Semi_Circle = input("Do you need semi circle calculations ")
if Semi_Circle == "Yes" or "yes":
    Diameter_Semi = float(input("Enter Diameter"))
    Radius_Semi = Diameter_Semi / 2 or float(input("Enter Radius"))
    Diameter_Semi = Radius_Semi * 2
    Circumference_Semi = (2 * pi * Radius)/2
    Area_Semi = pi*(Radius**2)/2

    print("Calculation complete")
    print(f"Diameter is {Diameter_Semi}")
    print(f"Radius is {Radius_Semi}")
    print(f"Circumference is {Circumference_Semi}")
    print(f"Area is {Area_Semi}")
else:
    exit()
"""
