#include <iostream>
#include <string.h>
using namespace std;
class Human {
public:
    string ID,name;
    Human(){
        ID="";
        name="";
    }
    void input(){
        cout << "Nhap thong tin\n";
        cout << "Nhap ID: ";
        getline(cin,ID);
        cout<< "Nhap ten: ";
        getline(cin,name);
    }
    void output(){
        cout << "\nThong tin: \n";
        cout << ID <<"\n"<<name;
    }
};
class Student : public Human{
public:
    int num;
    void Num (int num){
        this ->num= num;
    }
};
class Techer : public Human{
public:
    int num;
    void Num (int num){
        this ->num= num;
    }
};
int main(){
    Student A;
    Techer B;
    A.input();
    A.Num(20);
    B.input();
    B.Num(40);
    A.output();
    cout <<"\nStudent number: "<< A.num;
    B.output();
    cout <<"\nAgent number: "<< A.num;
 return 0;
}