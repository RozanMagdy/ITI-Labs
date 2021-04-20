number_list=list()
while(1):
    inPut=input('Enter a number: ')
    if inPut=='Done':
        break
    else:
        try:
            number_list.append(int(inPut))
        except:
            print("string input is not available")
print('Max is '+str(max(number_list)))
print('Min is '+str(min(number_list)))
    

