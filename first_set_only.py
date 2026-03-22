# Hex Colors
almost_white = "\033[38;5;16m"
reset = "\033[0m"
soft_red = "\033[38;5;210m"

# Removing all Unique num
print(f" {almost_white} \nENTER UNIQUE NUMBER ONLY {reset} ")

numbers = []

# Input 10 num
for i in range(10):
    num = int(input(f"Number {i+1}: {reset} "))
    numbers.append(num)

# Display all numbers
print("\nAll Numbers Entered:")
print(numbers)

# Remove duplicates keeping the first occurence
unique = []
seen = set()

for num in numbers:
    if num not in seen:
        unique.append(num)
        seen.add(num)

# Display results
print(f"{soft_red}\nNumbers with duplicate (First Entry Only): {reset} {unique}")