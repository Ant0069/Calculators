import math
import time
print("Welcome to the triangle identifier")
TIC = int(input("Press 1 for Angles or 2 for Sides "))
if TIC == 1:
   #Angle
   Angle_a = int(input("Enter Angle value of A "))
   Angle_b = int(input("Enter Angle value of B "))
   Angle_c = int(input("Enter Angle value of C "))
   #TV = total value
   TV = Angle_a + Angle_b + Angle_c
   if TV == 180:
       time.sleep(1)
   else:
      print("Error Angle must add up to 180")
      exit()
   
   if Angle_a == 0 or Angle_b == 0 or Angle_c == 0:
        print("Error value can't be zero")
        exit()
   #By Angle
   if Angle_a <90 & Angle_b <90 & Angle_c <90:
       print("This is a Acute Triangle")
       exit()
   elif Angle_a == 90 or Angle_b == 90 or Angle_c ==90:
       print("This is a Right Triangle")
       exit()
   elif Angle_a >90 or Angle_b >90 or Angle_c >90:
       print("This is a Otuse Triangle")
       exit()
   else:
       print("Error try again")
       exit()
   #By Side
elif TIC ==2: 
   print("C must always be the biggest value")
   print("Put zero if you have no value for C")
   Side_A = int(input("Enter value of side A "))    
   Side_B = int(input("Enter value of side B ")) 
   Side_C = int(input("Enter value of side C ")) 
   #Pythagorean Theorem
   if Side_C == 0:
       Ans = Side_A * Side_A + Side_B * Side_B   
       print(math.sqrt(Ans))
       print("That is the missing value")
   else: time.sleep(1)
   
   if Side_A == Side_B and Side_B == Side_C:
       print("This is a Equilateral Triangle")
   elif Side_A == Side_B or Side_B == Side_C or Side_A == Side_C:
       print("This is a Isoceles Triangle")
   elif Side_A != Side_B != Side_C:
       print("This is a Scalene Triangle")
        

else:
    print("Error try again")
    exit()
