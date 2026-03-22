#Enter Invalid Input Until Lower number display

#Displaying numbers
numbers = []
print("HIGHEST NUMBER")
print("(Invalid number will stop the program)")

#While-True function for output
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

    except ValueError:
        print("Invalid input! Stopping...")
        break

    except KeyboardInterrupt:
        print("\033[38;5;210m\nProgram Stopped Automatically. Thank you! \033[0m")
        break
# Final Output

if numbers:
    lowest_number = max(numbers)
    print(f"\nAll numbers entered: {numbers}")
    print(f"Highest number: {lowest_number}")