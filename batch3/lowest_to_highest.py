#LOWEST TO HIGHEST NUMBER

#Displaying numbers
numbers = []
print("ENTER NUMBERS (Invalid Input will stop the Program)")

while True:
    try:
#Ask User to input
        num = int(input("Enter a number: "))
        numbers.append(num)
        print(f" ✓ Added: {num}")
    except ValueError:
        print("Invalid input! Stopping...")
        break
    except KeyboardInterrupt:
        print("\033[38;5;210m\nProgram Stopped Automatically. Thank you! \033[0m")
        break

# Check if any numbers were entered

if not numbers:
    print("No valid numbers were entered!")
else:
    # Sort numbers from lowest to highest
    numbers.sort()
    
    print("\n SORTED NUMBERS (lowest to highest)")
    for i, num in enumerate(numbers, 1):
        print(f"{i}. {num}")
    
    print(f"\nTotal numbers: {len(numbers)}")
    print(f"Smallest: {numbers[0]}")
    print(f"Largest: {numbers[-1]}")