
string = "https://adventofcode.com/2024/day/1/input"
for items in string:
    left, right = map(int, items.split())
    list1.append(left)
    list2.append(right)
list1 = []
list2 = []
distance = 0
sumDistance = 0
for i in range(len(list1)-1):
    for j in range(len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
for i in range(len(list2)-1):
    for j in range(len(list2)-i-1):
        if list2[j] > list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]
for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])
    sumDistance += distance

