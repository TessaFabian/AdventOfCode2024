def task01(mylist):
    for i in range(len(mylist)-1):
        sub_mylist = mylist[i:i+2]
        if abs(sub_mylist[0]-sub_mylist[1]) < 1:
            return 0
        elif abs(sub_mylist[0]-sub_mylist[1]) > 3:
            return 0
    return 1

def task02(mylist):
    #Ansatz: gebe statt index die Liste zurück
    for i in range(len(mylist)-1):
        sub_mylist = mylist[i:i+2]
        if abs(sub_mylist[0]-sub_mylist[1]) not in range(1,4):
            # item at index i can be immediately removed from mylist
            return mylist.pop(i)
        elif abs(sub_mylist[0]-sub_mylist[1]) in range(1,4):
            #there's nothing to delete
            continue
    return mylist

def check_removable(level_diff1, level_diff2):
    #sind beide level im Intervall [1,3]?
    if level_diff1 in (1,4) and level_diff2 in (1,4):
        return True
    return False

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
    #print(mylist)
    #if check_isSorted(mylist):
        #number_safe_reports += task01(mylist)

    ##task 02
    mylist = task02(mylist)

#print("task 01: "+str(number_safe_reports))

