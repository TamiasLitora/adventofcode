#day 1
#the file containing data
inputFile = open("day1/input", "r")

bigger = 0
comparisonsMade = 0

#read in file to list, stripping newline and castin to ints
file = [int(i.strip()) for i in inputFile.readlines()]

for i in range(len(file)-2):

    if (file[i-1] + file[i] + file[i+1]) < (file[i] + file[i+1] + file[i+2]):
        bigger +=1

    comparisonsMade += 1


print("%s checks made, %s are bigger" % (comparisonsMade, bigger))
