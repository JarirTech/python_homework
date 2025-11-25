import traceback
import csv
#Task1: Diary



import traceback
try:
    # special line
    special_input = "done for now"
    with open('diary.txt', 'a') as file:

        # first input
        user_input1 = input("What happened today? \n")
        file.write(user_input1 + '\n')
        while True:
            # second input
            user_input = input('What else? \n')
            file.write(user_input + "\n")
            if user_input == special_input:
                break
            
except Exception:
    traceback.print_exc()   