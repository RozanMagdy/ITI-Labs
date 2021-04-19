file_name = input("Enter file Name: ")
f = open(file_name, "r")
lines=f.read().splitlines()
for line in lines:
    print(line.upper())