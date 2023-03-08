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

// struct по умолчанию public а class private
class Lecture {
public:
    //constructor по умолчанию чтобы юзать Lecture lec без параметров для lec
    Lecture(){
        name = "Vasya";
        duration = 123;
    }
    //заюзаем конструктор - Название такое же как и у класса (а также нет типа возвращаемого значения)
    Lecture (const string& new_name, const int& new_duration){
        //SetName(new_name);
        // SetDuration(new_duration);
        name = new_name;
        duration = new_duration;
    }





    //делаем публичную секцию чтобы ретривить поля
    public:
    //делаем метод константым, говоря, что он ен может поменять поля
    //таким образом мы сможем решить проблемы при вызове методов внутри методов с константной ссылкой

    void PrintLecture(const Lecture& lec){
        cout << lec.author << lec.author << lec.name;
    }
    //по константной ссылки можно вызвать только константный метод
    int GetDuration() const {return duration};
    string GetAuthor(){return author};
    void SetDuration(const int& new_duration){
        duration = new_duration;
        UpdateSmth();
    }
    void SetName(const string& name){
        this->name = name;
    }
    //создадим метод который сраз заполняем оба поля
    //такой метод не стандартизирован - поэтому используем конструкторы
    Lecture BuildLecture(const int& duration, const string& name) {
        Lecture lec;
        lec.SetDuration(duration);
        lec.SetName(name);
        return lec;
    }

private:
    void UpdateSmth(){

    }
    // делаем поля приватнымм
    // так нет прямого доступа к полям - только внутри scope
    private:
        int duration;
        string author;
        string name;
};

struct DetailedLecture{
    Lecture info;
    string week;
};


//Можем в ретурн закидывать стракт также без создания временной переменной
Lecture GetLecture (){
    return {123, "", ""};
}

int main() {
    Lecture lecture1;
    //не можем напрямую обратиться к полям
    lecture1.duration = 123;
    lecture1.author = "Kosmos";



    //другой способ инициализации (более компактный)
    Lecture lecture2 ={123, "Komos", "Karatis"};

    //можем передавть в функцию значения без создания временной переменной
    PrintLecture({123, "Komos", "Denis"});

    //constructor for string
    string stringa(10, 'a');

    DetailedLecture lec3 ={
            {123, "", ""},
            ""
    };
    return 0;
}