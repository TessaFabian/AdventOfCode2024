def task01(list_left, list_right):
    totaldistance = 0
    for x in range(len(list_left)):
        totaldistance += abs(list_left[x]-list_right[x])
    return totaldistance

file = open("input.txt", "r")
list_left = []
list_right = []
for line in file.read().splitlines():
    list_left.append(int(line.split()[0]))
    list_right.append(int(line.split()[1]))
list_left.sort()
list_right.sort()

print("Task 01: "+str(task01(list_left, list_right))) #Solution: 1889772