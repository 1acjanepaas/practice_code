# Take 10 inputs from the user
numbers = []
print("Enter 10 numbers")
for i in range(10):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num)

first_number = numbers[0]
remaining_sum = sum(numbers[1:])

# Perform calculation: first - (sum of others)
result = first_number - remaining_sum
print(f"Result ({first_number} - sum of others): {result}")