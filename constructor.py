class Faculty:
    def __init__(self, name="Unknown", department="General", salary=30000):
        self.name=name
        self.department=department
        self.salary=salary
    
    def display(self):
        print(f"Faculty Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: Rs.{self.salary}")


# object with user values
f1=Faculty("Dr. Patil", "Computer Science", 75000)

# object with default values
f2=Faculty()

print("Faculty 1 Details:")
f1.display()
print("\nFaculty 2 Details:")
f2.display()