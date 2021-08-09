import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
# print(a)
print("The new created array is : ", end=" ")
for i in range(0, 6):
    print(a[i], end=" ")

print()

# inserting array elements using insert()
# syntax:
#     list_name.index(index, element)

a.insert(1, 10)

print("Array after insertion : ", end=" ")
for i in a:
    print(i, end=" ")

print()

# using append function

a.append(9)

print("After using append : ", end="")

for i in a:
    print(i, end="  ")

print()

# accessing the element in the array

print("Access the element is : ", a[3])

# Removeing the elements
# syntax :
    # list_name.remove(object)

# pop()

# print("The popped element is : ", end="")
# print(a.pop(1))
#
print("After popping array is : ", end=" ")
for i in range(0, 6):
    print(a[i], end=" ")

print()

# a.remove(10)
#
# print("After removing array is : ", end=" ")
# for i in range(0, 6):
#     print(a[i], end=" ")


