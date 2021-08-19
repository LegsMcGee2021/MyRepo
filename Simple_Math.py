fn = int(input("First Number:"))
sn = int(input("Second Number:"))
sum = str(fn + sn)
dif = str(fn - sn)
pro = str(fn * sn)
if sn != 0:
    quo = str(fn/sn)
else:
    quo = "Undefined"
print("Sum: " + sum + " Difference: " + dif + " Product: " + pro + " Quotient: " + quo)
