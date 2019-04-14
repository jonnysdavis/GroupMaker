import random

if __name__ == "__main__":

    #Open text files
    roster_file = open("roster.txt", "r")
    banPairs_file = open("banned_pairs.txt","r")
    students = roster_file.readlines() #each line an element
    studentsNeedingGroup = students
    roster_file.close() #close text file
    bannedPairs = banPairs_file.readlines()
    banPairs_file.close()
    groups = [] #list to make groups in


    groupSize = input("How big is each group?")
    currentGroupSize = 0 #student number in current group

    count = 0
    for person in studentsNeedingGroup:
        if(count == 0):
            #if it's the first student, add them to group one
            groups.append(person)
            studentsNeedingGroup.remove(person)
        else:
            currentGroupSize = groups[count-1].count(',')
            randomNumber = random.randInt(0, len(studentsNeedingGroup))


            randomStudent = studentsNeedingGroup[randomNumber]
            canAdd = False

            while(canAdd == False):
                #check if student has any banned group mates
                if(randomStudent not in bannedPairs):
                    canAdd = True







        count+=1
