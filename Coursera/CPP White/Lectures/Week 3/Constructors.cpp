#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;


class Persona {
public:
    void PrintPersona(Persona()){
        cout << name << " " << age << ENDLINE;
    };

    void SetName (const string& new_name){
        name = new_name;
    }

    Persona(){
        age = 24;
        name = "Vaverin";
    }
    Persona(const string& new_name, const int& new_age){
        age = new_age;
        name = new_name;
    }
    //деструктор который вызвается при уничтожении объекта
    //как только объектт выходит из под зоны видимости то он уничтожается
    //вызовом деструктора
    ~Persona(){
        cout << "Thank you!";
    }
private:
    //можем назначить age=0 как дефолтное значение
    string name;
    int age;
};

struct Shlyapa{
    int size = 12;
};

int main(){
    Persona persona;
    Persona persona1("asd", 123);
    //передаём персону 1
    persona1.PrintPersona({});
    //всё равно печатаем персону1
    persona1.PrintPersona({});
    //Печатаем стандартный класс
    Persona().PrintPersona();
    return 0;
}