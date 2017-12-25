def circle(r):
	area=3.14*r*r
	print("Area  :", area)
  
def rectangle(l,b):
	area=l*b
	print("Area :",area)
  
def triangle(b,h):
	area=0.5*b*h
	print("Area  :",area)
def main():
	r=int(input("Enter radius for circle :\n"))
	circle(r)
	print("\n ----Rectangle----\n")
	l=int(input("Enter length :\n"))
	b=int(input("Enter breadth :\n"))
	rectangle(l,b)
	print("\n----Triangle---- \n")
	b=int(input("\nEnter Breadth  :\n"))
	h=int(input("Enter Height  :\n"))
	triangle(b,h)
