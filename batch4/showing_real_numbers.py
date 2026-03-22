print("SHOWING DUPLICATE NUMBER")
number = []

# Input 10 nunber
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)

# Find duplicates   
seen = set()
duplicates = set()

for num in number:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(f"All nunber: {number}")
print(f"Duplicate nunber: {sorted(list(duplicates))}")