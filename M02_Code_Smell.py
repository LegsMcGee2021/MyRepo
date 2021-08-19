uncle_sam = 1.08
pay_the_server = 1.15
food_stuff= float(input("How much was your meal? "))
corprate_cut = uncle_sam * food_stuff
pocket_book_pain = str(corprate_cut * pay_the_server)
print("You need to leave " + pocket_book_pain + " on the table to cover tax and tip.")
