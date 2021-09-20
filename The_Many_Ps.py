names = []
prices = []

def av():
    sum = 0
    for x in prices:
        sum += x
    p = len(prices)
    sum /= p
    return sum

while True:
    name = input("What is your name:\n")
    names.append(name)
    price = input("How much was your food:\n")
    prices.append(float(price))
    loop = input("Is there another person? Y/n\n")
    if loop == "Y" or loop == "" or loop =="y":
        continue
    elif loop == "N" or loop == "n":
        break

average = av()
print(f"The average cost was {average}\n")
for n in names:
    for p in prices:
        if p > average:
            difference = p - average
            print(f"Hello {n}, your total was above average by {difference}")
        elif p < average:
            difference = average - p
            print(f"Hello {n}, your total was below average by {difference}")
        elif p == average:
            print(f"Hello {n}, your total was equal to the average")
