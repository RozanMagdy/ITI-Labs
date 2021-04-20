while(1):
    string = input("enter your string: ")
    if string =='q':
        break
    for i in string:
        if i in ['A', 'E', 'I', 'O', 'U', 'a','e','i','o','u']:
            string=string.replace(i,'')
    print(string)