from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():
    s1 = Student("Gary", 85)
    s2 = Student("Chris", 90)
    s3 = Student("Kevin", 88)
    s4 = Student("Jessie", 89)
    s5 = Student("Norm", 75)
    s6 = Student("Erica", 20)
    s7 = Student("Mary", 100)
    s8 = Student("James", 92)
    s9 = Student("Dan", 35)
    s10 = Student("Anne", 86)

    roster = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    result = average_grade(roster)
    print(f"{result}")

if __name__ == "__main__":
    main()
