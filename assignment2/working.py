import assignment2 as a2
import os
import custom_module
import csv
from datetime import datetime

# #Task 15: Write Out Sorted List

def  write_sorted_list():
    
    sorted_lst = sorted(a2.minutes_list, key= lambda x: x[1])
    
    conv_lst = list(map(
        
    lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_lst
    ))
    
    with open('./minutes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(a2.minutes1["fields"])
        for row in conv_lst:
            writer.writerow(row)
    print(conv_lst)
    return conv_lst

write_sorted_list()
