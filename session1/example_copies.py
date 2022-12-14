# shallow copy gone right
li = [3, 4, 12]
li2 = li.copy()

li2[0] = 5

print(li, li2)

# shallow copy gone wrong
li3 = [1, 2]
li4 = [3, 4]
li5 = [5, 6]

list_of_lists1 = [li3, li4, li5]
list_of_lists2 = list_of_lists1.copy()

list_of_lists1[0][0] = 10

print(list_of_lists1, list_of_lists2)