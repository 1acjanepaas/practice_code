# Program to print all numbers between two user-input numbers

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"\nNumbers between {num1} and {num2}:")
print("=". * 30)

# Handle both cases: num1 < num2 or num2 < num1
if num1 < num2:
    # Print numbers from num1+1 to num2-1
    for i in range(num1 + 1, num2):
        print(i)
elif num2 < num1:
    # Print numbers from num2+1 to num1-1
    for i in range(num2 + 1, num1):
        print(i)
else:
    print("No numbers between same values!")

print("=". * 30)