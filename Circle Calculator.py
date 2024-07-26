import math
import tkinter as tk
from tkinter.simpledialog import askstring
pi = math.pi

Windows = tk.Tk()
Windows.title("Circle Calculator")
Windows.geometry("200x200")
Diameter = float(askstring("Diameter", "Enter diameter "))
Radius = Diameter/2 or float(askstring("Radius", "Enter Radius "))
Diameter = Radius * 2
Circumference = 2*pi *Radius or float(askstring("Circumference", "Enter Circumfernce "))
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

Windows_Semi = tk.Tk()
Windows_Semi.title("Semi Circle Calculator")
Semi_Circle = str(askstring("Semi Circles", "Do you need semi circle calculations ")).lower
if Semi_Circle == "yes":
   Diameter_Semi = float(askstring("Diamter", "Enter Diameter"))
   Radius_Semi = Diameter_Semi/2 or float(askstring("Radius", "Enter Radius"))
   Diameter_Semi = Radius_Semi * 2
   Circumference_Semi = (2 * pi * Radius_Semi)/2
   Area_Semi = pi*(Radius_Semi**2)/2

   semi_Diameter_Ans = tk.Label(text=f"Diameter is {Diameter_Semi}")
   Semi_Radius_Ans = tk.Label(text=f"Radius is {Radius_Semi}")
   Semi_Circumfernce_Ans = tk.Label(text=f"Circumfernce is {Circumference_Semi}")
   Semi_Area_Ans = tk.Label(text=f"Area is {Area_Semi}")

   semi_Diameter_Ans.pack()
   Semi_Radius_Ans.pack()
   Semi_Circumfernce_Ans.pack()
   Semi_Area_Ans.pack()
else:
   exit()


