#This will be the project file

# Open text file
f = open('test.txt', 'r')
n = open('uploadfile.xml','w')
# while not end of text file
for line in f:
    print 'this is'
    print line
    n.write(line)
# write to new wp xml file in correct wrappers
print n.readline()
# endwhile
# save new xml file with same name as text file
