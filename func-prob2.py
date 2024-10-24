# Write a python code using functions to calculate area and perimeter of a circle and rectangle.

s=input("Enter the shape: ").lower()

pi=22/7

def circleArea(radius):
  area=pi*radius**2
  return int(area)

def circumference(radius):
  circ=2*pi*radius
  return int(circ)

def rectangleArea(length, width):
  area=length*width
  return area

def perimeter(length, width):
  perim=2*(length+width)
  return perim

if s=="circle":
  c=input("Enter what you want to calculate: ").lower()
  radius=int(input("Enter the radius of the circle: "))
  if c=="area":
    print(f"{circleArea(radius)} sq. units")
  elif c=="perimeter":
    print(f"{circumference(radius)} units")
elif s=="rectangle":
  c=input("Enter what you want to calculate: ").lower()
  l=int(input("Enter length of the rectangle: "))
  w=int(input("Enter width of the rectangle: "))
  if c=="area":
    print(f"{rectangleArea(l,w)} sq. units")
  elif c=="perimeter":
    print(f"{perimeter(l,w)} units")
elif s=="exit":
  print("Stop Execution")