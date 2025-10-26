"""I wrote this program because it connects to what we learned in class
about Charles Darwin and natural selection. The program shows how animals with
stronger traits survive and pass those traits to the next generation,
just like in real evolution.
This project also connects to me personally because I love technology and coding, and
I wanted to use those skills to explain a science concept in a fun and easy way.
By writing this program, I was able to combine two things I enjoy — learning about
nature and using computers to model how it works.
It’s a simple way to show that even small changes over time can lead to big differences,
which is what evolution is all about.
"""

# 💻 Code: “Survival of the Fittest”

import random

print("🐒 Welcome to the Survival Game!")
print("Let's see how animals change over time...\n")
# Step 1: Make a starting group of animals
animals = []
for i in range(10):
    strength = random.randint(1, 10)
    animals.append(strength)
print("Starting animals (their strength from 1–10):")
print(animals)
print()
# Step 2: Repeat for 5 generations
for generation in range(1, 6):
    print("🌿 Generation", generation)
    # The strong animals survive (those >= average strength)
    average_strength = sum(animals) / len(animals)
    survivors = [a for a in animals if a >= average_strength]
    # If everyone is weak, keep at least 1 alive
    if len(survivors) == 0:
        survivors.append(random.choice(animals))
    print("Survivors:", survivors)
    # The survivors have babies (new animals like them)
    babies = []
    while len(babies) < 10:
        parent = random.choice(survivors)
        # Baby strength is like parent, with small change
        baby_strength = parent + random.choice([-1, 0, 1])
        baby_strength = max(1, min(10, baby_strength))  # Keep it between 1–10
        babies.append(baby_strength)
        animals = babies  # The new generation replaces the old one
        print("New Generation:", animals)
        print("Average strength:", round(sum(animals) / len(animals), 2))
        print()
print("🏆 The animals have gotten stronger over time!")
