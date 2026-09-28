# Now we'll increase the difficulty.

# Create this dataset:

# import numpy as np

# np.random.seed(60)

# marks = np.random.randint(30, 101, (20, 5))

# Think of:

# 20 students × 5 subjects
# Task

# Using NumPy only:

# Print the indexes of these students.
# Print their average marks.

import numpy as np

np.random.seed(60)

marks = np.random.randint(30, 101, (20, 5))
print(marks)

# Calculate the average marks for every student.

avg_std_marks = np.mean(marks,axis=1)
print("avg marks of the student : ",avg_std_marks)

# Find students whose average is greater than or equal to 75.
students = avg_std_marks[avg_std_marks >= 75]
print("Students with average >= 75:", students)

# Find students who have failed in at least one subject.
# Fail = marks < 40

student_failed =  marks < 40
print("student_failed : ",len(student_failed))

# Find students who passed every subject AND have average >= 75.

students_passed = np.where(np.all(marks > 40, axis=1) & (avg_std_marks >= 75))[0]
print("students_passed: ",students_passed)

# Print the indexes of these students.

std_marks = np.column_stack((np.arange(len(marks)), marks))
print(std_marks)


# Print their average marks.
print("Their average marks:", avg_std_marks[students_passed])