even_numbers = list(range(2,11,2))   #start, stop, step
print (even_numbers)

num_list = [4,5,6,7,8]
num_list2 = list(range(4,9))
a_tuple = (4,)  #same with list but can't modify, add ',' if its only one
print(type(a_tuple))
b_tuple = tuple([4,5,6])


squares = []
tubes = []
for value in range (1,11):
    square = value**2
    squares.append(square)
    tube = value**3
    tubes.append(tube) #tubes.append(value**3)

print(f"square list {squares}")
print(f"tube list {tubes}")

#list comprehension- generate the same list in one line of code
square_list = [value**2 for value in range (1,11)]
print(square_list)