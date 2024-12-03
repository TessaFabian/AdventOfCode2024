def task01(mylist):
    for i in range(len(mylist)-1): #könnte out of bounce geben
        sub_mylist = mylist[i:i+2]
        print(str(sub_mylist))
        if abs(sub_mylist[0]-sub_mylist[1]) < 1:
            return 0
        elif abs(sub_mylist[0]-sub_mylist[1]) > 3:
            return 0
    return 1
            

def check_isSorted(mylist):
    mylist_asc = sorted(mylist)
    mylist_desc = sorted(mylist, reverse=True)
    if mylist_asc == mylist or mylist_desc == mylist:
        return True
    else:
        return False



file = open("input02.txt", "r")
number_safe_reports = 0
number_isSorted = 0
for line in file.read().splitlines():
    mylist = [int(number) for number in line.split()]
    #überprüfe sortierung --> muss dec oder asc sein
    #wenn sortierung eingehalten wurde:
        #Any two adjacent levels differ by at least one and at most three
    if check_isSorted(mylist):
        number_isSorted += 1
        number_safe_reports += task01(mylist)
print("task 01: "+str(number_safe_reports))
print(number_isSorted)