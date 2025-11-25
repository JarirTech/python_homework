import traceback
import csv    
import os
import custom_module
from datetime import datetime

#Task 2: Read a CSV File
def read_employees():
    my_dict = {}
    my_list = []
    try:
        with open('../csv/employees.csv', newline='') as csvfile:
            data = csv.reader(csvfile) 
            for index, row in enumerate(data):
                if index == 0: # store the first row in the dict using the key "fields"
                    my_dict["fields"]=row
                else: #Add all the other rows (not the first) to your rows list.
                    my_list.append(row)
        #print(my_dict)
        #print(my_list)
        my_dict["rows"]=my_list #Add the list of rows (this is a list of lists) to the dict, using the key "rows".
                
                               
    except Exception:
        traceback.print_exc()

    return my_dict

employees = read_employees()
print(employees)


#Task 3: Find the Column Index

def column_index(value):
    for val in employees['fields']:

        val = employees['fields'].index(value)
    #print(val)
    return employees['fields'].index(value)
        
#employee_id_column = column_index()
employee_id_column = column_index("employee_id")


#Task 4: Find the Employee First Name

def first_name(num):
    first_name_index = column_index("first_name")
    for index, row in enumerate(employees['rows']):
        if index == num:
            #print(row[first_name_index])
            return row[first_name_index]
        

# Task 5:

def employee_find(employee_id):
    
    employee_id_column = column_index("employee_id")

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches= list(filter(employee_match, employees["rows"]))
    # print(matches)
    # print(len(matches))
    return matches

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   print(matches)
   return matches

#Task 7: Sort the Rows by last_name Using a Lambda
employee_last_name_column= column_index("last_name")

def sort_by_last_name():
    sorted_list = sorted(employees['rows'], key =lambda row: row[employee_last_name_column])
    #print(sorted_list)
    return sorted_list



#Task 8: Create a dict for an Employee

def employee_dict(row):

    dict_header = employees['fields'][1:]
    
    new_dict = {k: None for k in dict_header}
  
    new_dict_val = row[1:]
    #print(new_dict_val)
    new_dict = dict(zip(dict_header, new_dict_val))
    #print(new_dict)
    return new_dict


#Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    all_dict = {}

    for row in employees['rows']:
        employee_id = row[0]          
        all_dict[employee_id] = employee_dict(row)
    print(all_dict)
    return all_dict

#Task 10: Use the os Module

def get_this_value():
    #print(os.environ.get('THISVALUE'))
    return os.environ.get('THISVALUE')


#Task 11: Creating Your Own Module

def set_that_secret(new_str):
    new_sec = custom_module.set_secret(new_str)
    #print(new_sec)
    return new_sec
#Task 12: Read minutes1.csv and minutes2.csv

minutes1 ={}
minutes2 ={}
def read_minutes():
    global minutes1 
    global minutes2 
    minutes1_list_val = []
    minutes2_lst = []
    #../csv/minutes1.csv and ../csv/minutes2.csv
    with open('../csv/minutes1.csv', newline='') as csvf:
        minutes1_data = csv.reader(csvf)

        for index, row in enumerate(minutes1_data):
            if index ==0:
                minutes1["fields"]=tuple(row)
            
            else:
                minutes1_list_val.append(tuple(row))
    minutes1['rows']= minutes1_list_val

    #print(f' minutes 1: \n {minutes1}')
    with open('../csv/minutes2.csv', newline='') as csvfile:
        minutes2_data = csv.reader(csvfile)
                
        for i, row in enumerate(minutes2_data):
            if i==0:
                minutes2['fields']= tuple(row)
            else:
                minutes2_lst.append(tuple(row))
    minutes2['rows']= minutes2_lst
   
    return  minutes1, minutes2

# Task 13: Create minutes_set

def create_minutes_set():
    set_minutes1=set(minutes1['rows'])
    #print(set_minutes1)
    set_minutes2 = set(minutes2['rows'])
    #print(set_minutes2)

    resulting_set = set_minutes1.union(set_minutes2)
    return resulting_set 
read_minutes()
global minutes_set
minutes_set = create_minutes_set()



#Task 14: Convert to datetime
def create_minutes_list():
    
    lst = list(minutes_set ) # converting the set object to list
    converted_row = map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), lst

    )
    resulting_lst = list(converted_row)
    return resulting_lst
minutes_list = create_minutes_list()


# #Task 15: Write Out Sorted List

def  write_sorted_list():
    
    sorted_lst = sorted(minutes_list, key= lambda x: x[1])
    
    conv_lst = list(map(
        
    lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_lst
    ))
    
    with open('./minutes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(minutes1["fields"])
        for row in conv_lst:
            writer.writerow(row)
    print(conv_lst)
    return conv_lst

