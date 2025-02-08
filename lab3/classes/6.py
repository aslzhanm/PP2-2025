class Student:
    def __init__(self, name, roll_number):
        self.name = name  
        self.roll_number = roll_number  
        self.grades = []  
    
    def add_grade(self, grade):
        self.grades.append(grade) 
        print(f"Added grade {grade} for {self.name}")

    def average_grade(self):
        if not self.grades:
            print(f"{self.name} has no grades yet.")
            return 0
        avg = sum(self.grades) / len(self.grades) 
        print(f"Average grade for {self.name}: {avg:.2f}")
        return avg

    def show(self):
        print(f"Student: {self.name}, Roll Number: {self.roll_number}")
        print(f"Grades: {self.grades}")


s1 = Student("Alice", 101)
s1.show()           
s1.add_grade(85)   
s1.add_grade(90)    
s1.add_grade(78)
s1.average_grade()  
s1.show()           
