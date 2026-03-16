#While loop
odd = []
i = 1
while i <= 100:
    if i % 2 != 0: #putting into one line only
        odd.append(i)
    i += 1
print(f"The old numbers are: ", odd)