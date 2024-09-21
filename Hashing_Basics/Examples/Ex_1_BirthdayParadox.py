import math

num_people = int(input("Enter number of people: "))
comparisons = (num_people * (num_people - 1)) // 2
not_same = (364 / 365)
chances = 1 - math.pow(not_same, comparisons)
print("Chances that there is a same birthday = ", round(chances * 100, 2), "%")
