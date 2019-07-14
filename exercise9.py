#Exercise 9.1.1
grocery_list = ["apples", "carrots", "oranges", "salmon"]
for item in grocery_list:
    print("* " + item)

# Exercise 9.1.2
grocery_list.append("rice")
print(grocery_list)

# Exercise 9.1.3
def display(my_list):
    for item in my_list:
        print("* " + item)
display(grocery_list)

# Exercise 9.2
print(len(grocery_list))

# Exercise 9.3
if "bananas" in grocery_list:
    print("You don't need to pick up bananas today")
else:
    print("You need to pick up bananas")

# Exercise 9.4
print(grocery_list[1])

# Exercise 9.5
grocery_list.sort()
display(grocery_list)

# Exercise 9.6
grocery_list.remove("salmon")
display(grocery_list)










