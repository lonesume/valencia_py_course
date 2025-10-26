year = int(input("What year is your truck? (Enter 0 to exit) "))

while year != 0:

    if year <= 2010 or year >= 2021:
        print("We only buy model years 2011 through 2020.")
    elif year <= 2015:
        print("We will offer $15000 for your truck.")

    else:
        print("We will offer $22000 for your truck.")
    year = int(input("What year is your truck? (Enter 0 to exit) "))

print("Thank for coming to Joseph Automotives Sales")
