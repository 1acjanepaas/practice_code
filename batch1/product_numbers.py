#Hex color for changing of colors
khaki = "\033[38;5;186m"
reset = "\033[0m"

#Title of the program
print (f"{khaki}\PRODUCT OF 2 NUMBERS\n{reset}")

#Printing of two numbers 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))

#Sum of numbers
result = num1 * num2
print("Product:", result)