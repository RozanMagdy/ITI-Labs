import numpy as np 
mylist=list()
for i in range(2,11):
    mylist.append(i)
x = np.array(mylist)
x = x.reshape(3,3)
print(x)