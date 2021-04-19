n=int(input('Please enter pyramid Hieght:'))
k = 2*(n - 1)
for i in range(0,2*n,2):
    for j in range(3, k):
        print(" ",end=" ")
    k = k - 1
    for j in range(0, i+1): 
        print("*", end=" ")
    print("\r")
 
