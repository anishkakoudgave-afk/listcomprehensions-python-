import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    index = random.randint(0, len(chars) - 1)
    password += chars[index]

print("Password:", password)