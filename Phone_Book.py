names = []
numbers = []
email = []

while True:
    names.append(input("Hi, what is your name?\n"))
    numbers.append(input("What is your phone number?\n"))
    email.append(input("What is your email?\n"))
    x = input("Are you finished? \nY/n: ")
    if x == "" or x == "Y" or x == "y":
        break
    elif x == "n" or x == "N":
        continue

with open("Contacts.txt", "a") as file:
    for x, y, z in zip(names, numbers, email):
        file.write(f"{x} {y} {z}\n")

