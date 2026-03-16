#While loop
print("Numbers without zero and five")
except_numbers = []
i = 1
while i <= 100:
    if not (str(i).endswith('0') or str(i).endswith('5')):
        except_numbers.append(str(i))
    i += 1
print(' '.join(except_numbers))