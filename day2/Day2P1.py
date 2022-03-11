#day 2
#the file containing data
import re
inputFile = open("day2/input", "r")

y = 0
x = 0

#read in file to list
file = inputFile.readlines()

for line in file:
    #splits command to direction/ amount
    line = line.split(' ')
    #checks first letter, because i prefer it aethetically
    match line[0][0]:
        case 'f':
            x += int(line[1])
        case 'd':
            y += int(line[1])
        case 'u':
            y -= int(line[1])

print("%s x, %s y, %s x*y"% (x, y, x*y))
