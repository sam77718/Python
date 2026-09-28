# */
# def analyze_employees(employees):
#     ...

# Given:

# employees = [
#     {"name": "Rahul", "department": "IT", "salary": 55000},
#     {"name": "Priya", "department": "HR", "salary": 45000},
#     {"name": "Amit", "department": "IT", "salary": 75000},
#     {"name": "Sneha", "department": "Finance", "salary": 65000},
#     {"name": "Kiran", "department": "HR", "salary": 50000},
#     {"name": "Arjun", "department": "Finance", "salary": 80000}
# ]

# Your function should:

# 1. Find the highest-paid employee

# Expected:

# Arjun
# 2. Find the lowest-paid employee

# Expected:

# Priya
# 3. Calculate the average salary

# Calculate the average salary of all employees.

# 4. Calculate average salary by department

# Expected structure:

# {
#     "IT": 65000,
#     "HR": 47500,
#     "Finance": 72500
# }
# 5. Find the highest-paying department

# Expected:

# Finance
# 6. Give each employee a salary category

# Rules:

# salary >= 70000 → "High"
# salary >= 50000 → "Medium"
# salary < 50000  → "Low"

# For example:

# {
#     "name": "Arjun",
#     "salary": 80000,
#     "category": "High"
# }
# 7. Return everything in one dictionary

# Something like:

# {
#     "highest_paid": "Arjun",
#     "lowest_paid": "Priya",
#     "average_salary": ...,
#     "department_averages": {...},
#     "highest_paying_department": "Finance",
#     "employees": [...]
# }
# 🔥 Extra challenge

# Handle:

# employees = []
# Missing salary
# Negative salary
# Two employees having the same highest salary
# An employee belonging to a new department not seen before*/


employees = [
     {"name": "Rahul", "department": "IT", "salary": 55000},
     {"name": "Priya", "department": "HR", "salary": 45000},
     {"name": "Amit", "department": "IT", "salary": 75000},
     {"name": "Sneha", "department": "Finance", "salary": 65000},
     {"name": "Kiran", "department": "HR", "salary": 50000},
     {"name": "Arjun", "department": "Finance", "salary": 80000}
 ]

def analyze_employees(employees):

# 1. Find the highest-paid employee
    highest = employees[0]
    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

# 2. Find the lowest-paid employee
    lowest = employees[0]
    for emp in employees:
        if emp["salary"] < lowest["salary"]:
            lowest = emp

# 3. Calculate the average salary          
    for emp in employees:
        total_sal = sum(emp["salary"] for emp in employees)
        avg = total_sal / len(employees)

# 4.  Calculate average salary by department
    
    department_averages = {}

    for emp in employees:
        dept = emp["department"]

        if dept not in department_averages:
            department_averages[dept] = []

        department_averages[dept].append(emp["salary"])


    # Convert salary lists into averages
    for dept, salaries in department_averages.items():
        department_averages[dept] = sum(salaries) / len(salaries)

# 5. Find the highest-paying department

    highest_paying_department = max(
        department_averages,
        key=department_averages.get
    )

# 6. Give each employee a salary category
    for emp in employees:
        if emp["salary"] >= 70000:
            emp["category"] = "High"
        elif emp["salary"] >= 50000:
            emp["category"] = "Medium"
        else:
            emp["category"] = "Low"

    result = {
        "highest_paid": highest["name"],
        "lowest_paid": lowest["name"],
        "average_salary": avg,
        "department_averages": department_averages,
        "highest_paying_department": highest_paying_department,
        "employees": employees
    }

    return result

result = analyze_employees(employees)
print(result)

  