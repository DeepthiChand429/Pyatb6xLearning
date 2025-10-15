#write a python program to calculate the area of circle
#give radius using the formula
#area=pi*r2

#i/p in r should be float
#o/p-string formatted out of area

#Logic building formula
radius=float(input("Enter your radius:\n "))
pi=3.1476810

area=pi*pow(radius,2) #area=3.14*(radis**2)--same
print("Area of circle is->", area) #o/p: Area of circle is-> 314.768

#String data formatting, python f-strings or formatted string literals--Replace data value
print(f"Area of circle is-> {area:.2f}") #o/P:Area of circle is-> 314.77