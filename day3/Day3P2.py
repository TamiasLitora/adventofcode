#day 3
def moreMatch(numbers, starting, moreLess):
    #for comparisons
    startingMatch = starting
    startingMatch += '1'
    matchCount = 0
    totalCount = 0
    returner = ''
    for line in numbers:

        if line.startswith(starting):
            if line.startswith(startingMatch.strip()):
                matchCount += 1
            totalCount += 1
            returner = line


    if totalCount == 1:
        return returner
    if moreLess == 'm':
        if matchCount >= (totalCount/2):
            return True
        else:
            return False
    else:
        if matchCount >= (totalCount/2):
            return False
        else:
            return True

#the file containing data
inputFile = open("day3/input", "r")

#read in file to list
file = inputFile.readlines()
oxyNumber = ''
carNumber = ''
oxyBreak = True
carBreak = True
for i in range(len(file[0].strip())):
    if oxyBreak:
        store = moreMatch(file, oxyNumber, 'm')
        if store == True:
            oxyNumber += '1'
        elif store == False:
            oxyNumber += '0'
        else:
            oxyNumber = store
            oxyBreak = false
    if carBreak:
        store = moreMatch(file, carNumber, 'l')
        if store == True:
            carNumber += '1'
        elif store == False:
            carNumber += '0'
        else:
            carNumber = store
            carBreak = False

oxyRate =  ''.join(str(i) for i in oxyNumber)
carRate = ''.join(str(i) for i in carNumber)
oxyRate = int(oxyRate, 2)
carRate = int(carRate, 2)
print("%s %s %s"% (oxyRate, carRate, oxyRate*carRate))
