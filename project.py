
num = int(input("Enter a number: "))

odd_numbers = [x for x in range(num) if x % 2 != 0]

even_numbers = [x for x in range(num) if x % 2 == 0]

print("Odd numbers under", num, ":", odd_numbers)
print("Even numbers under", num, ":", even_numbers)

fruits = ["apple", "banana", "mango", "orange", "grape"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruit list:", fruits)
print("Capitalized fruit list:", capitalized_fruits)