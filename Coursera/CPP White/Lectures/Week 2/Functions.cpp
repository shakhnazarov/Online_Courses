#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

//можем замерять работу программы
#include <chrono>
using namespace std;
using namespace std::chrono;

int Sum(int x, int y) {
    return x + y;
}


// Так мы можем изменять значение самой переменной
// с помощью ссылки Int&
void Swap (int& x, int& y) {
    int temp = x;
    x = y;
    y = temp;
}


void Sort (vector<int>& vec) { // изменили тото вектор который хотелт
    sort(begin(vec), end(vec));
}

// по константной ссылке мы бы смогли в функцию сразупередать результат вызова другой функции
void PrintThis (const int& x) {
    cout << x;
}

struct Person {
    string name;
    int age;
};

int main() {
    //два измерителя времени начало и конец
    auto start = steady_clock::now();


    //рекурсивные алгоритмы можно организовать только в функции
    // functions have local variables not global ones
    vector<int> a = {1, 4, 3};
    Sort(a);


    auto finish = steady_clock::now();

    cout << duration_cast<microseconds>(finish-start).count();

    // мы не можем передать результат вызова функции по ссылке
    // function(giveMeResult()) где в фfunction передаётся ссылка - не сработает


    //const modifier можем добавить и к переменным тогда не сможем менять их
    const vector<int> tit = {1, 2, 3};
    //в контейнере элементы тоже не сможем поменять
    return 0;
}