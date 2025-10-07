number_of_bicycles = int(input())

""" Your code goes here """
if number_of_bicycles > 46:
    print("Need multiple racks")
if 12 <= number_of_bicycles <= 46:
    print("Large bike rack")
elif 0 < number_of_bicycles <= 11:
    print("Small bike rack")
elif number_of_bicycles <= 0:
    print("Bad input")
