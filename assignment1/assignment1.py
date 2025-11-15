
# Task1: Hello 


def hello():
    
    #print("Hello!")
    return "Hello!"

hello()



def greet(name):
    #print(f"Hello, {name}!")

    return f"Hello, {name}!"
greet("James")

#Task 3: Calculator

def calc(val1, val2, operation="multiply"):
    try:

        if operation == "add":
            result = val1+ val2
            #print(result)
            return result
        
        elif operation == "subtract":

            result = val1 - val2
            #print(result)
            return result
        elif operation == "multiply":
            result = val1 * val2
            #print(result)
            return result
        elif operation == "divide":
            try: 
                result = val1/val2
                #print(result)
                return result
            except ZeroDivisionError:
                #print("You can't divide by 0!")
                return "You can't divide by 0!"
                
        elif operation == "modulo":
            result = val1 % val2
            #print(result)
            return result
        elif operation == "int_divide":
            try:
                result = val1//val2
                #print(result)
                return result
            except ZeroDivisionError:
                #print("You can't divide by 0!")
                
                return "You can't divide by 0!"
        elif operation == "power":
            result = val1 **val2
            #print(result)
            return result
    except TypeError:
        #print(f"You can't {operation} those values!")
   

        return f"You can't {operation} those values!"

    
# Task 4: Data Type Conversion



def data_type_conversion(val, typ: str):
    try:
        if typ == "str":
            result = str(val)
            # print(type(result).__name__)
            # print(result)
            type(result).__name__
            return result
        elif typ == "float":
            result = float(val)
            # print(type(result).__name__)
            # print(result)
            type(result).__name__
            return result
        elif typ == "int":
            result = int(val)
            # print(type(result).__name__)
            # print(result)
            type(result).__name__
            return result
    except:
        return f"You can't convert {val} into a {typ}."
    
# Task 5: Grading System, Using *args

def grade(*args):
    try:
        average = sum(args)/len(args)
        print(average)
        if average >= 90:
            grade = "A"
            #print(grade)
            return grade
        elif 80<= average <= 89:
            grade = "B"
            #print(grade)
            return grade
        elif 70 <= average <= 79:
            grade = "C"
            #print(grade)
            return grade
        elif 60<= average <= 69:
            grade = "D"
            #print(grade)
            return grade
        else: 
            grade = "F"
            #print(grade)
            return grade

    
    
    except:
        return "Invalid data was provided."

#Task 6: Use a For Loop with a Range
def repeat(par1: str, par2:int):
    new_word = ""

    for word in range(par2):
        new_word += par1
        
    #print(new_word)
    return new_word
# Task 7: Student Scores, Using **kwargs

def student_scores(*args, **kwargs):
   
    grade = args[0]  

    if grade == "best":
        highest_score = max(kwargs.values())
        
        returned_name= next(k for k, v in kwargs.items() if v == highest_score) 
        print(returned_name)
        return returned_name

    elif grade == "mean":
        average = sum(kwargs.values())/len(kwargs.values())
        print(average)
        return average
        
    else :
        raise ValueError("invalid entry")

#Task 8: Titleize, with String and List Operations
def titleize(par:str):
    
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words =par.split()
    #print(words)
    
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            words[i]= word.capitalize()
        else:
            if word not in little_words:
                words[i] = word.capitalize()
            else:
                words[i] = word.lower()
        
        new_string = " ".join(words)
    #print(new_string)
    return new_string

#Task 9: Hangman, with more String Operations

def hangman(secret, guess):
    secret_word = ""
    for i, char in enumerate(secret):

        if char in guess:
            secret_word += char
        else:
            secret_word += "_"
    #print(secret_word)
    return secret_word

#Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(text):
    vowels = ["a", "e", "i", "o", "u"]
    words = text.split()
    outputs = []

    for word in words:
        if not word:
            outputs.append("")
            continue

        # start with "qu"
        if word.startswith("qu"):
            outputs.append(word[2:] + "qu" + "ay")
            continue

        result = ""
        for i, char in enumerate(word): #"square"
            
            if i + 1 < len(word) and word[i] == "q" and word[i + 1] == "u":
                # Move the entire cluster up to and including 'u'
                cluster = word[: i + 2]       # include 'qu'
                rest = word[i + 2 :]
                result = rest + cluster + "ay"
                break

            # 1) "apple"
            if i == 0 and char in vowels:
                result = word + "ay"
                break

            # 2) "banana"
            if i == 0 and char not in vowels:
                if len(word) > 1 and word[1] in vowels:
                    result = word[1:] + word[0] + "ay"
                    break
                

            # 3) "cherry"
            if i == 1 and char not in vowels and word[0] not in vowels:
                # If third letter exists and is vowel -> move two-letter cluster
                if len(word) > 2 and word[2] in vowels:
                    result = word[2:] + word[0] + word[1] + "ay"
                    break
                # If word length == 2, swap them
                if len(word) == 2:
                    result = word[1:] + word[0] + "ay"
                    break
                # otherwise continue to handle longer clusters

            # 4) General cluster end: if we reached a vowel after initial consonants
            if i > 0 and char in vowels:
                cluster = word[:i]
                rest = word[i:]
                result = rest + cluster + "ay"
                break

        # If nothing matched  move whole word + "ay"
        if not result:
            result = word + "ay"

        outputs.append(result)

    #print(" ".join(outputs))
    return " ".join(outputs)
