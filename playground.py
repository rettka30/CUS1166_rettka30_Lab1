print("Basic program: ")
print("\nHello Word")
# Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))
# Alternative way to format a string
print("Hello %s" % myname)
print("Done Practicing The Basic Program")

print("\nVariables: ")
i = 120
print(f"\nVariable i has the value {i}")
f = 1.6180339
print(f"Variable f has the value {f} and its type is {type(f)}")
b = True
print(f"Variable b has the value {b}")
n = None
print(f"Variable n has the value of {n}")
# tuple
c = (10,20,10)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")
# list
l = ["Anna", "Tom", "John"]
l = [10,20,30]
print(f" l[0] has the value {l[0]} and is of type: {type(l)}")
# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)
# Dictionary
grades = {"Tom" : "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"
# Create an empty dictionary .
mydictionary = dict()
print("Done Practicing Variables")

print("\nConditionals: ")
x=10
if (x > 0):
    print("\nThe number x is positive")
elif (x<0):
    print("\nThe number x is negative")
else:
    print("\nThe number x is zero")
print("Done Practicing Conditionals")

print("\nLoops: ")
for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )
print("Done Practicing Loops")

print("\nFunctions: ")
def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False
print("Done Practicing Functions")

print("\nClasses: ")
class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", " + self.isbn)
print("Done Practicing Classes")
