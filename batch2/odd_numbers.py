print("Odd Numbers from 0 to 100")

num = 1  # Start at first odd number

while num <= 100:
    print(num, end=" ")  # end=" " prints horizontally
    num += 2  # Jump by 2 (1→3→5→7...)

print()  # New line at end
print(f"Total odd numbers: {(100+1)//2}")  # 50 odds!