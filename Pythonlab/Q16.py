f = open('mbox-short.txt', "r")
lines=f.read().splitlines()
count=0
for line in lines:
    if line[0:5]=="From ":
        count=count+1
        line_list=line.split()
        print(line_list[1])
print('Number of lines is '+str(count))        