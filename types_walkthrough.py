name = input("What is your name?")

print(f"Hello {name}")

print("Per the Cleveland Clinc, you should eat 2000 calories a day.")

caloricIntake = int(input("How many calories have you consumed tody?"))

caloriesNeeded = 2000 - caloricIntake 

# print(f"You need to eat another {caloriesNeeded} calories today.")

# print(name,type(name))
# print(caloriesNeeded,type(caloriesNeeded))

if caloriesNeeded > 0 :
    print(f"You need to eat another {caloriesNeeded} calories today.")
    if caloriesNeeded <= 0 :
        print(f"You need to eat another {caloriesNeeded} calories today.")

players ={
    "Lebron James" : 23,
    "Lamar Jackson" : 8
}

print(players)
print(type(players))
print(players["Lebron James"])
print(type(players["Lebron James"]))
