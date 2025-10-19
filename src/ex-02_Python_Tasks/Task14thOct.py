#area=1/2*base*height
#take b 10 and h=5 float result
base=float(input('Enter base:'))
height=float(input('Enter height:'))
area=0.5*base*height
print(f"Area of triangle is-> {area:.2f}")
#check if a number entered by user is greater than 100
number=int(input('Enter number:'))
"""if number>100:
    print("Is number greater than 100")
else:
    print("Is number less than 100")"""
print("Is number greater than 100" if number>100 else "Is number less than 100")