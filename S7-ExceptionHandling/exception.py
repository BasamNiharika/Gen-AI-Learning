# Exception Handling:

# Exceptions are the events that disturbs the normal flow of the program. They occur when an error is encountered during program 
# execution: Common Example includes
# 1. Zero Division Error 
# 2. File Not Found Error 
# 3. Value Error
# 4. Type Error 

# Exception try, except block
try:
    a = b
except:
    print("The variable has not been assigned")

try:
    a = b
except NameError as ex:
    print(ex) 

try:
    result = 1/0
except ZeroDivisionError as ex:
    print(ex)

# try:
#     result = 1/2
#     a=b   #throws error
# except ZeroDivisionError as ex:
#     print(ex)

try:
    result = 1/2
    a=b  
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)

try:
    num = int(input("enter the number:"))
    result = 10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than zero.")
except Exception as ex:
    print(ex)

# try, else, except block
try:
    num = int(input("enter the number:"))
    result = 10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than zero.")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")

# finally block 
try:
    num = int(input("enter the number:"))
    result = 10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than zero.")
except Exception as ex:
    print(ex)
finally:
    print("Execution Complete")



