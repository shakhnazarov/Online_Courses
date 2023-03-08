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


struct Lecture {
    int duration;
    string author;
    string name;
};

struct DetailedLecture{
    Lecture info;
    string week;
};
void PrintLecture(const Lecture& lec){
    cout << lec.author << lec.author << lec.name;
}

//Можем в ретурн закидывать стракт также без создания временной переменной
Lecture GetLecture (){
    return {123, "", ""};
}

int main() {
    Lecture lecture1;
    lecture1.duration = 123;
    lecture1.author = "Kosmos";

    //другой способ инициализации (более компактный)
    Lecture lecture2 ={123, "Komos", "Karatis"};

    //можем передавть в функцию значения без создания временной переменной
    PrintLecture({123, "Komos", "Denis"});

    DetailedLecture lec3 ={
            {123, "", ""},
            ""
    };
    return 0;
}