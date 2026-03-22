#Printing numbers
even_numbers = []
print("Enter 10 numbers")

#Printing even numbers with a twist
for i in range (10):
    while True:
        try:
            number = int(input(f"Number {i+1}: ")) #While loop
            if number % 2 == 0:
               even_numbers.append(number)
            break
        except ValueError: #To accept the code
            print("\033[31m Invalid input!\033[0m Please enter a number only.") #For changing the color

print("The even numbers entered are: ", even_numbers) 
#To print the output
