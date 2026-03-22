# Removing all Unique numbers
print("\nENTER UNIQUE NUMBER ONLY")

numbers = []

# Input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Remove duplicates (keep first occurrence)
unique = []
seen = set()

for num in numbers:
    if num not in seen:
        unique.append(num)
        seen.add(num)

# Display results
print(f"\nAll numbers: {numbers}")
print(f"Unique numbers: {unique}")
print(f"Duplicates removed: {len(numbers) - len(unique)}")