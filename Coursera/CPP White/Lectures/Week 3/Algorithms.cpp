#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

bool Gt2(int x){
    return x>2;
}

int main() {
    vector<int> col {
        1, 3, 4, 124, 2
    };
    int threshold = 10;
    cout << count_if(col.begin(), col.end(), Gt2 );
    //Можем вместо этого использовать лямбда функцию
    //квадратные скобки говорят о лямбда выражении, внутру них переменные которые хотим заснут в скоуп функции
    cout << count_if(col.begin(), col.end(), [threshold] (int x){
        return x>threshold;
    });

    //C++ приследует принцип "zero overhead principle"
    // мы не заполняем переменную дефолтным значением потому что дорого

    //Значения перменной следуют инициализировтаь из-за прицнипа выше
    // можно инициалзировать черзе функцию или чрезе тернарный оператор
    return 0;
}