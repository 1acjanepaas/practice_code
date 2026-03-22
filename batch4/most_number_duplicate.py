from collections import Counter
# MOST NUMBER DUPLICATE

# Hex Colors
mint_color = "\033[48;5;158m"
reset = "\033[0m"
italic_text = "\033[03;5;231m" # Just a little extra >.<

# Putting Some title 
print("\nMOST NUMBER DUPLICATE\n")
numbers = []

# Continuous input until invalid
while True:
    num = input("Enter Number: ")
    try:
        num = input(f"✓ Added: {num} | New number: ")
        if not num:
            continue # To continue the output without getting error
        
        new_num = int(num)
        numbers.append(new_num)

        print(f"{italic_text} {mint_color} ✓ Added successfully! Total: {len(numbers)} {reset}") #Highlighted ++ Italic Text

    except ValueError:
        print("Invalid input! Stopping...")
        break
    except KeyboardInterrupt:
        print("Program Stopped by User. Good bye!")
        break

if not numbers:
    print("No valid numbers entered!")
else:
    # Count frequencies
    count = Counter(numbers)
    
    # Find number with most duplicates
    most_common_num = count.most_common(1)[0][0]
    max_count = count.most_common(1)[0][1]
    
    print(f"\nAll numbers: {numbers}")
    print(f"Frequency: {dict(count)}")
    print(f"\n🏆 Number with MOST duplicates: {most_common_num}")
    print(f"Appears {max_count} times!")