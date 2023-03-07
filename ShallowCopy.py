import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list_copy = copy.copy(old_list)
new_list_copy2 = old_list[:]


old_list[1][1] = 'AA'

print('changing exist')
print("Old list:", old_list)
print("New list:", new_list_copy)
print("New list2:", new_list_copy)

old_list.append([15])
old_list[1].append(15)
print('new stuff')
print("Old list:", old_list)
print("New list:", new_list_copy)
print("New list2:", new_list_copy)
