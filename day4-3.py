fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen_lol = [fruits, vegetables, ["Kiwi"]]

print(dirty_dozen_lol)

# Option 1
dirty_dozen_l = []
for i in range(len(dirty_dozen_lol)):
    dirty_dozen_l.extend(dirty_dozen_lol[i])

# Option 2 - much better
dirty_dozen_l_1 = []
for elem in dirty_dozen_lol:
    dirty_dozen_l_1.extend(elem)


print(dirty_dozen_l)
print(dirty_dozen_l_1)