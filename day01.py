def task01(list_left, list_right):
    totaldistance = 0
    for x in range(len(list_left)):
        totaldistance += abs(list_left[x]-list_right[x])
    return totaldistance

def task02(list_left, list_right):
    score = 0
    for index in range(len(list_left)):
        score += list_left[index]*list_right.count(list_left[index])
    return score


file = open("input.txt", "r")
list_left = []
list_right = []
for line in file.read().splitlines():
    list_left.append(int(line.split()[0]))
    list_right.append(int(line.split()[1]))
list_left.sort()
list_right.sort()

print("Task 01: "+str(task01(list_left, list_right))) #Solution: 1889772
print("Task 02: "+str(task02(list_left, list_right))) #Solution: 23228917