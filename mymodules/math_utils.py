from mymodules.models import Student

def average_grade(roster):
    sum = 0
    index = 0
    for i in range(len(roster)):
        sum += roster[i].get_grade()
        index += 1
    ave = sum/index
    return ave

def square(x):
    return x*x
