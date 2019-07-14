# Exercise 10.1
students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}

# Exercise 10.2
def display(my_dict):
    for key, num in my_dict.items():
        print("In ", key, "there are ", num, " students")
display(students)

# Exercise 10.3
students['cohort4'] = 43

# Exercise 10.4
print(list(students.keys()))

# Exercise 10.5
for key, value in students.items():
    new_value = value + (value * 0.05)
    students[key] = round(new_value)
display(students)

# Exercise 10.6 
del students['cohort2']
display(students)

# Exercise 10.7  
sum = 0
for value in students.values():
    sum += value
print(sum)


