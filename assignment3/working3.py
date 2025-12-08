import logging

#Task 1: Writing and Testing a Decorator

#2Declare a decorator called logger_decorator:
# logger set up
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(fun):
    def func_wrapper(*args, **kwargs):
        
        if args !=None:
            pos_parms = args
        else:
            pos_parms = None
        if kwargs !=None:
            kw_parms = kwargs
        else:
            kw_parms = None
        # loging fun name and parameters
        logger.log(logging.INFO, f"function: {fun.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_parms}")
        logger.log(logging.INFO, f"keyword parameters: {kw_parms}")

        result = fun(*args, **kwargs)
        # logging result
        logger.log(logging.INFO, f'return: {result}')
        return result
    return func_wrapper

#3:Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". 
# Decorate this function with your decorator.
@logger_decorator
def hello_world():
    print('Hello, World!')

hello_world()

#4.Declare a function that takes a variable number of positional arguments and returns True.
#  Decorate this function with your decorator.
@logger_decorator
def var_num(*pos_parms):
    return True

var_num(6,7,8)

#5.Declare a function that takes no positional arguments and a variable number of keyword arguments,
#  and that returns logger_decorator. Decorate this function with your decorator.
@logger_decorator
def log_dec(**kw_parms):
    return logger_decorator

log_dec(state ="MA", city= "Boston", zipcode = "02108" )

#---------------------------------------------------------------------------------------------------------------


# Task 2: A Decorator that Takes an Argument