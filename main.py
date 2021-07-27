
#1
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList = [12, 35, 9, 56, 24]
print(swapList(newList))


#2
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))


#3
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 16
print('{} has occurred {} times'.format(x, countX(lst, x)))


#4
L = [4, 5, 1, 2, 9, 7, 10, 8]
count = 0

for i in L:
    count += i
avg = count / len(L)
print("sum = ", count)
print("average = ", avg)


#5
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


#6
# list of numbers
list1 = [2, 7, 5, 64, 14]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
print("\n")

#7
list2 = [2, 7, 5, 64, 14]
for num2 in list2:
    if num2 % 2 != 0:
        print(num2, end=" ")


#8
list1 = [2, 7, 5, 64, 14]
even_count, odd_count = 0, 0
for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("\nEven numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#9
list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num >= 0:
        print(num, end=" ")
print("\n")


#10
list1 = [12, -7, 5, 64, -14]
for num in list1:
    if num < 0:
        print(num, end=" ")
