#Inputing 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Ensuring the numbers in between
if num1 > num2:
    num1, num2 = num2, num1

result = []
i = num1 + 1
while i < num2:
    result.append(str(i))
    i += 1
#To print the result
if result:
    print(' '.join(result))
else:
    print("No numbers between them")