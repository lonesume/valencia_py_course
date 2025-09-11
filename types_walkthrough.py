name = input("What is your name? ")


print(f"Hello {name}")

print("Per the Cleveland Clinc, you should eat 2000 calories a day.")

# caloricIntake = int(input("How many calories have you consumed tody?"))

while True:
    try:
        caloricIntake = int(input("How many calories have you consumed today? "))
        break   #  Exit loop if input is valid
    except ValueError:
        print(" Invalid input! Please enter a number.")

caloriesNeeded = 2000 - caloricIntake

if caloriesNeeded > 0:
    print(f"You need to eat another {caloriesNeeded} calories today.")
if caloriesNeeded <= 2000:
    print("You have met or exceeded your 2000 calorie goal today!")
else :
    print("you need to eat 2000 calories today")
# print(name,type(name))
# print(caloriesNeeded,type(caloriesNeeded))
# if caloriesNeeded > 0 :
#     print(f"You need to eat another {caloriesNeeded} calories today.")
#     if caloriesNeeded <= 0 :
#         print(f"You need to eat 2000 calories today.")

players ={
    "Lebron James" : 23,
    "Lamar Jackson" : 8
}

print(players)
print(type(players))
print(players["Lebron James"])
print(type(players["Lebron James"]))
