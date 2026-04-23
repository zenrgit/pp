import matplotlib.pyplot as plt
import numpy as np

# Sample Dataset (Marks of students)
marks = [45, 55, 65, 70, 75, 80, 85, 90]
students = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# -------- Bar Chart --------
plt.figure()
plt.bar(students, marks)
plt.title("Bar Chart - Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()

# -------- Histogram --------
plt.figure()
plt.hist(marks, bins=[30,40,50,60,70,80,90,100])
plt.title("Histogram - Marks Distribution")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()