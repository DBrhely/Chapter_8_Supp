#Chapter 8-1
#2/18/15
#Danielle Brhely

class Rectangle(object):
    def __init__(self,ID,width,length):
        self.name = ID
        self.name1 = ID1
        self.name2 = ID2
        self.width = int(input("What is the width of this side? "))
        self.length = int(input("What is the length of this side? "))
        
    def __str__(self):
        rep = "Rectangle object\n"
        rep += "ID: " + self.name + "\n"
        print("Rectangle ID: ", self.name)
        print("Rectangle ID1: ", self.name1)
        print("Rectangle ID2: ", self.name2)
        print("Length: ", self.length)
        print("Width: : ", self.width)
        
    def perimeter(self):
        perimeter = 2*self.length + 2*self.width
        print("Perimeter: ", perimeter)
        return perimeter
    
    def area(self):
        area = self.length * self.width
        print("Area: ", area)
        return area

#main
choice = None
choice = int(input("Enter a choice number....")) 
print("""
Quit - 0
Length - 1
Width - 2
""")
while choice != 0:
      if choice == 1:
          self.length
          print(self.length)
      elif choice == 2:
          self.width
          print(self.width)
      else:
          print("Invaild answer.")
