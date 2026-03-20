#Color Hex for Changing of Colors
lime_green = "	\033[38;5;82m"
reset = "\033[0m"

#Inputting the numbers
print (f"{lime_green}\nBIGGER NUMBER\n{reset}")

first_num = int(input(f"Enter the first number: "))
second_num = int(input("Enter the second number: "))

#Defining the bigger number using if-else
if first_num > second_num:
    print("The biggest number is", first_num)
elif first_num < second_num:
    print("The biggest number is", second_num)