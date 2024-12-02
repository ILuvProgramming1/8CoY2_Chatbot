list1 = [9,8,7,6,5,4,3,2,1]
list2 = []
for i in range(len(list1 -1)):
    for j in range(len(list1 - i - 1)):
        if list1[j] > list1[i+1]:
            data[i+1] = data[j]
print(list1)
