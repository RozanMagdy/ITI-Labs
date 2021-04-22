import math
f = open('python_test_file.txt', "rt")
lines=f.read().splitlines()
Data=''
for line_index in range(len(lines)):
    sum=0
    if lines[line_index].split(',')[16] !='        ':
        sum=sum+float(lines[line_index].split(',')[16][3:])**2
    if lines[line_index].split(',')[17] !='        ':
        sum=sum+float(lines[line_index].split(',')[17][3:])**2
    if lines[line_index].split(',')[18]!='        ':
        sum=sum+float(lines[line_index].split(',')[18][3:])**2
    #print(line_index,round(sum, 3))
    string = ',Speed,   ' + str(round(math.sqrt(sum), 3))+'\n'
    lines[line_index]=lines[line_index]+ string
    #print(lines[line_index])
    Data=Data+ lines[line_index]
f.close()
f = open('python_test_file.txt', "wt")
#overrite the input file with the resulting data
f.write(Data)
#close the file
f.close()

