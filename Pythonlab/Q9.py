class my_calss():
    def get_String (self):
        string=input('enter your string: ')
        return string
    def print_String (self,String):
        return String.upper()

myclass=my_calss()
string=myclass.get_String()
print(myclass.print_String(string))