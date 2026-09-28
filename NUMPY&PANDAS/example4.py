# 🟦 Question 4 — NumPy | Advanced

# Create this dataset:

# np.random.seed(40)

# data = np.random.randint(1, 101, (10, 5))

# Think of it as:

# 10 students × 5 subjects
# Task

# Using NumPy only:

# Helpful functions

# You may need:

# np.mean()
# np.argmax()

import numpy as np

np.random.seed(40)

data = np.random.randint(1, 101, (10, 5))
print("Data (10 students * 5 subjects):\n", data)

# Find the average marks of each student.

student_average = np.mean(data, axis=1)
print("student average",student_average)

# Find the average marks of each subject.

subject_average = np.mean(data, axis=0)
print("subject average", subject_average)

# Find the student with the highest average.

high_std_avg = max(student_average)
print("highest student avg ",high_std_avg)

# Find the subject with the highest average.

high_sub_avg = max(subject_average)
print("highest subject avg ",high_sub_avg)

# Print the student index and their average.

std_result = np.column_stack((np.arange(len(student_average)), student_average))
print(std_result)

# Print the subject index and its average.

sub_result = np.column_stack((np.arange(len(subject_average)), subject_average))
print(sub_result)
