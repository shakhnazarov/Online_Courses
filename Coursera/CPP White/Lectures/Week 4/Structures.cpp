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

struct Day{
    int value;

    //используем explicit, чтобы не было implicit преобразований из Int в Day
    explicit Day(const int& new_value){
        value = new_value;
    };
};

struct Month{
    int value;
    Month(const int& new_value){
        value = new_value;
    };
};

int main(){
    Month month = {1};
    Month month1 = {Month(1)};
    //не работает так как нам explicitly Нужно задать тип, например, чтобы не путаться
    //Day day = {1};


    return 0;
}