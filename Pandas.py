import pandas as pd

students_data = pd.DataFrame({
    "Name":   ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age":    [20,      22,    19,       21,     20],
    "Grade":  ["A",     "B",   "A",      "C",    "B"],
    "Marks":  [85,      78,    92,       65,     74]
})

print("Student Data:")
print(students_data)
print("-" * 30)


print("First 3 rows:")
print(students_data.loc[0:2])
print("-" * 30)


print("Name and Marks:")
print(students_data[["Name", "Marks"]])
print("-" * 30)


print("Students with Grade 'A':")
print(students_data[students_data["Grade"] == "A"])