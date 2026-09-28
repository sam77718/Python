# def analyze_students(students):
#     ...

# The input is a list of dictionaries:

# students = [
#     {"name": "Rahul", "marks": [85, 90, 78, 92]},
#     {"name": "Priya", "marks": [45, 55, 60, 50]},
#     {"name": "Amit", "marks": [95, 88, 91, 97]},
#     {"name": "Sneha", "marks": [30, 40, 35, 45]}
# ]

# Your function should:

# Calculate the average marks of every student.
# Assign a grade:
# 90+ → "A"
# 75–89 → "B"
# 60–74 → "C"
# 40–59 → "D"
# Below 40 → "F"
# Find the student with the highest average.
# Find the student with the lowest average.
# Calculate the class average.
# Return a dictionary like:
# {
#     "students": [...],
#     "top_student": "...",
#     "lowest_student": "...",
#     "class_average": ...
# }

from unicodedata import name


students = [
    {"name": "Rahul", "marks": [85, 90, 78, 92]},
    {"name": "Priya", "marks": [45, 55, 60, 50]},
    {"name": "Amit", "marks": [95, 88, 91, 97]},
    {"name": "Sneha", "marks": [30, 40, 35, 45]}
]   

def analyze_students(students):
    student_data = []
    for std in students:
        marks = std["marks"]
        avg = sum(marks)/len(marks)


        if avg >= 90:
           grade = "A"
           
        elif avg >= 75:
           grade = "B"  
        elif avg >= 60:
           grade = "C"
        elif avg >= 40:
           grade = "D"
        elif avg < 40:
           grade = "F"
        else:
           grade = "not sat for the exam"

        student_data.append({
            "name": std["name"],
            "average": avg,
            "grade": grade
        })

    highest = students[0] 
    for std in students:
       if sum(std["marks"])/len(std["marks"]) > sum(highest["marks"])/len(highest["marks"]):
          highest = std

    lowest = students[0]
    for std in students:
        if sum(std["marks"])/len(std["marks"]) < sum(lowest["marks"])/len(lowest["marks"]):
            lowest = std


    class_avg = sum(sum(std["marks"])/len(std["marks"]) for std in students) / len(students)

    result = {
        "students": student_data,
        "top_student": highest["name"],
        "lowest_student": lowest["name"],
        "class_average": class_avg
    }

    return result
    
result = analyze_students(students)
print(result)

 