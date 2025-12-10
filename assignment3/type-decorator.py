
#Declare a decorator called type_converter. It has one argument called type_of_output, 
# which would be a type,like str or int or float. It should convert the return 
# from func to the corresponding type, viz:
#x = func(*args, **kwargs)
#   return type_of_output(x)
def type_converter(type_of_output):
    def decorator_fun(func):
        
        def wrapper_func(*args, **kwargs):
            x= func(*args, **kwargs)
            return type_of_output(x)
        return wrapper_func
        
    return decorator_fun
#3. Write a function return_int() that takes no arguments and returns the integer value 5.
#  Decorate that function with type-decorator.
@type_converter(str)

def return_int():
    return 5

str_result =return_int()
print(type(str_result)) # <class 'str'>

#4. Write a function return_string() that takes no arguments and returns the string value "not a number".
#  Decorate that function with type-decorator. In the decoration, pass int as the parameter to 
# type_decorator. Think: What's going to happen?

@type_converter(int)
def return_string():
    return "not a number"

# int_result = return_string()
# print(type(int_result))   # ValueError: invalid literal for int() with base 10: 'not a number'

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen

