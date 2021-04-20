def even_check(num_lits):
    even_list=list()
    for i in num_lits:
        if i%2==0:
            even_list.append(i)
    return even_list        
print(even_check([3,9,5,4,5,18,7,18,19]))