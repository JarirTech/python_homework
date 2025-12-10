import csv
#Task 3: List Comprehensions Practice

#2. Add code that reads the contents of ../csv/employees.csv into a list of lists using the csv module.

with open('../csv/employees.csv', newline='') as csvfile:
    lst_data = csv.reader(csvfile)

# 2.Using a list comprehension, create a list of the employee names, first_name + space + last_name. 
# The list comprehension should iterate through the items in the list read from the csv file. Print
#  the resulting list. Skip the item created for the heading of the csv file.
    list_lst = []
    for index, row in enumerate(lst_data):
        if index !=0:
            list_lst.append(row)
    #print(list_lst)

    lst_employees= [row[1:3] for row in list_lst]
    lst_employees_names= [f_name + " " + l_name for f_name, l_name in lst_employees]
    print(lst_employees_names)

    #3. Using a list comprehension, create another list from the previous list of names. This list should include
    #  only those names that contain the letter "e". Print this list.
    e_names_lst = [name for name in lst_employees_names if "e" in name]
    print(e_names_lst)

