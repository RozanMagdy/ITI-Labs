// Your First C++ Program

#include <iostream>
void Q1 (void){
    int num;
    std::cout << "Enter number between 1 to 100: ";
    std::cin >> num;
    if (num == 24){
        std:: cout << num << " is my faviourit number";
        std:: cout << "\n";
    }
    else{
        std:: cout << num << " is not my nfaviourit number";
        std:: cout << "\n";
    }
}
void Q2 (void){
    int num,reversedNumber = 0, remainder;
    std::cout << "Enter number: ";
    std::cin >> num;
    while(num!= 0) {
        remainder = num%10;
        reversedNumber = reversedNumber*10 + remainder;
        num/= 10;
    }
    std::cout << "Reversed Number = " << reversedNumber;
    std:: cout << "\n";
}
void Q3(void){
    int arr[5];
    int * ptr;
    int i =0;
    ptr = arr;
    
     for (i =0; i<=4;i++){
        std::cout << "Enter number = ";
        std::cin >> arr[i];
    }
    std::cout << "You entered :1";
    std:: cout << "\n";
    for (i =0; i<=4;i++){
        std::cout << *(ptr+i);
        std:: cout << "\n";
    }
}
void Q4 (void){
    int arr[5];
    int i =0;
    int max=0;
    for (i =0; i<=4;i++){
        std::cout << "Enter number "<< (i+1) <<":";
        std::cin >> arr[i];
    }
    for (i =0; i<=4;i++){
        if (arr[i]>max){
            max=arr[i];
        }
    }
    std::cout << "Largest element is :" << max;
    std:: cout << "\n";
}
void Q5 (void){
    int arr[5];
    int i =0;
    int sum=0;
    for (i =0; i<=4;i++){
        std::cout << "Enter number "<< (i+1) <<":";
        std::cin >> arr[i];
    }
    for (i =0; i<=4;i++){
        sum=sum+arr[i];
    }
    std::cout << " Average is :" << (sum/5.0);
    std:: cout << "\n";
}

class Mycalss {        // The class
  public:          // Access specifier
    int first_num;  // Attribute
    int second_num;  // Attribute
    Mycalss(int x , int y ) { // Constructor with parameters
      first_num = x;
      second_num = y;
    }
    int addtion(void){
        return first_num+second_num;
    }
};
void Q6(void){
    int num1,num2,sum=0;
    std::cout << "Enter number one: ";
    std::cin >> num1;
    std::cout << "Enter number Two: ";
    std::cin >> num2;
    Mycalss myobject(num1, num2);
    sum=myobject.addtion();
    std::cout << "  The addtion result is: " << (sum);
    std:: cout << "\n";
}

class complex{        // The class
  public:          // Access specifier
    int real1;  // Attribute
    int imagenery1;  // Attribute
    int real2;  // Attribute
    int imagenery2;  // Attribute
    complex(int x , int y, int z, int l) { // Constructor with parameters
      real1= x;
      imagenery1 = y;
      real2= z;
      imagenery2 = l;
    }
    int add_real(){
        return real1+ real2;
    }
    int add_imagenry(){
         return imagenery1+ imagenery2;
    }

};
void Q7(void){
    int num1R,num1I,num2R,num2I,sum=0;
    std::cout << "Enter number one: "<<'\n';
    std::cout << "Enter number one real part: ";
    std::cin >> num1R;
    std::cout << "Enter number one imaginary part: ";
    std::cin >> num1I;
    std::cout << "Enter number Two: "<<'\n';
    std::cout << "Enter number two real part: ";
    std::cin >> num2R;
    std::cout << "Enter number two imaginary part: ";
    std::cin >> num2I;
    complex numbers(num1R, num1I,num2R, num2I);
    std:: cout << "sum of real part: " << numbers.add_real();
    std:: cout << "\n";
    std:: cout << "sum of imaginary part: " << numbers.add_imagenry();
    std:: cout << "\n";
}


int main() {
    //Q1();
    //Q2(); 
    //Q3();
    //Q4();
    //Q5();
    //Q6();
    //Q7();
    return 0;
}

