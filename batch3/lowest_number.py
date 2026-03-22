#Enter Invalid Input Until Lower number display

#Displaying numbers
numbers = []
print("ENTER NUMBERS (Invalid Input will stop the Program)")

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
        print(f"Added: {num}")
    except ValueError:
        print("Invalid input! Stopping...")
        break
    except KeyboardInterrupt:
        print("\033[38;5;210m\nProgram Stopped Automatically. Thank you! \03\033[0m")
        break
if numbers:
    lowest_number = min(numbers)
    print(f"\nAll numbers entered: {numbers}")
    print(f"Lowest number: {lowest_number}")