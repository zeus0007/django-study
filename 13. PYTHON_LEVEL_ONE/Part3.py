# Lists
mylist = [1, 2, 3]
mylist = ['stringasdf', 1, 2, 3, 23.2, True, [1, 2, 3]]

print(len(mylist))

mylist = ['a', 'b', 'c']
print('before : ')
print(mylist)
mylist[0] = 'NEW ITEM'
print("after :")
print(mylist)
mylist.append(["x", "y", "z"])
print(mylist)
mylist.extend(["x", "y", "z"])
print(mylist)
mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop()
print(mylist)
print(item)
mylist.reverse()
mylistNumber = [4, 6, 1, 7, 43, 2]
mylistNumber.sort()

mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2][0])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][0]

# list comprehension
first_col = [row[0] for row in matrix]

print(first_col)
