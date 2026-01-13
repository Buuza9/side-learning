# """
# Basically, exceptions in Python are abnormally terminate
# the execution of the pytohn program. Since exception anormally
# terminate the exceution of the program, it is important to
# handle these exceptions. In Python, we use try .. except
# caluse/block to handle exception.
# """

# # 1. Try ... except Block, we place the code that
# # might cause an error inside the try block, and every
# # try block is followed by an except block, when an exception occurs,
# # it is caught by the execpt block.
# # The execpt block cannot be used without the try block
# #Syntax:
# try:
# 	#the code may cause exception.
# except:
# 	#code should be run when the exception occurs
# 	None

# #Example:
# try:
# 	numerator = 10
# 	denominator = 0

# 	result = numerator / denominator

# 	print(result)
# except:
# 	print("Error: Denominator cannot be 0.")

# Exception: An evet that interrupts the flow of the program,
# (ZeroDivisionError, TypeError, ValueError)

# 1. try 2. except 3. finally


# try:
# 	number = int(input("Enter a number: "))
# 	print(1 / number)
# except ZeroDivisionError:
# 	print("Number cannot be divded by zero.")
# except ValueError:
# 	print("Please enter a valid data type!")

try:
	number = int(input("Enter a number: "))
	print(1 / number)
except ZeroDivisionError:
	print("Number cannot be divded by zero.")
except ValueError:
	print("Please enter a valid data type!")
except Exception:
	print("Something went wrong.")
finally:
	print("Do some cleanup.")