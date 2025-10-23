# 1. List of students
Students = {"Name": "Alice", "Grades": [85, 90, 78]}, {"Name": "Bob", "Grades": [70, 65, 80]}, {"Name": "Charlie", "Grades": [95, 88, 92]}

# 2. Print name and average
for Student in Students:
    Average = sum(Student["Grades"]) / 3
    print(f"{Student['Name']}: {Average:.1f}")