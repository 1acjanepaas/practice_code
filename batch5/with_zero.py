# Input number (0-1000)
num = int(input("Enter number (0-1000): "))

# Validate range
if 0 <= num <= 1000:

# Convert to string and pad with zeros (width=6)
    formatted_num = str(num).zfill(6)
    print(f"Input:  {num}")
    print(f"Output: {formatted_num}")

else:
    print("Invalid! Number must be 0-1000")