print("Duplicate Checker (Enter 'q' to quit")
seen = set()  # Track unique numbers

while True:
    user_input = input("\nEnter a number (or 'q' to quit): ")
    
    # Check if input is invalid (quit)
    if user_input.lower() == 'q':
        print("Goodbye, Have a nice day!")
        break
    
    # Try to convert to number
    try:
        num = int(user_input)
        
        # Check for duplicate
        if num in seen:
            print(f"{num} → DUPLICATE!")
        else:
            print(f"{num} → UNIQUE!")
            seen.add(num)
            
    except ValueError:
        print("Invalid input! Enter a number or 'q' to quit.")
        break

print(f"\nTotal unique numbers: {len(seen)}")