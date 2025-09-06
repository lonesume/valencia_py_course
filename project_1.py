# Using PyCharmLinks to an external site. or another IDE of your choosing, 
# implement a short Python program that utilizes random number generationLinks to an external site.
# , the modulo operatorLinks to an external site, and
# at least one operation from the math moduleLinks to an external site..
# Details beyond this are up to you.




import random
import math 

x =  random.randint(100, 100000)
y =  random.randint(100, 100000)


x = math.sqrt(x)
y = math.sqrt(y)

z = x/y
remainder = x % y

print(f"This is X: {x}")
print(f"This is Y: {y}")
print(f"This is Z: {z}")
print(f"Remainder: {remainder}")