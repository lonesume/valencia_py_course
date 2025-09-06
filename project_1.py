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