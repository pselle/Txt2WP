from sys import argv

script, input_file = argv

# Create the upload file and the list
n = open('uploadfile.xml','w')
a = []

# put the lines in a list
with open(input_file,'r') as f:
    for line in f:
        #ignore empty lines
        if(line != '\n'):
            a.append(line)
            n.write(line)

#Splice the list in sets of items
x = len(a)
y = 5
b = a[:y]
c = a[y+1:y+6]
d = a[y+y+2:x-y-1]
e = a[x-y:x]
print b,c,d,e
# write to new wp xml file in correct wrappers

# save new xml file with same name as text file
