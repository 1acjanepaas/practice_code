fullname = input("Enter fullname: ")

print("Choose cleaning:")
print("1. lstrip()  - Remove LEADING spaces only")
print("2. rstrip()  - Remove TRAILING spaces only")
print("3. strip()   - Remove BOTH leading + trailing")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    result = fullname.lstrip()
elif choice == "2":
    result = fullname.rstrip()
elif choice == "3":
    result = fullname.strip()
else:
    result = fullname

print(f"Result: '{result}'")