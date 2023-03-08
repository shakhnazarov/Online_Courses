#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <fstream> //для работы с потоками
#include <iomanip> //для работы с  fixed выводом
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

struct Duration{
    int mm;
    int ss;

    Duration(const int& mm=0, const int& ss=0){
        int total = mm*60+ss;
        this -> mm = total/60;
        this -> ss = total%60;
    }
};

Duration ReadDuration(istream& is){
    Duration duration;

}

void PrintDuration(ostream& ost, const Duration& duration){
    ost << setfill('0');
    ost << setw(2) << duration.mm << ":" << setw(2) << duration.ss;
}

//Можем перегрузить оператор вместо функции принтдурешн


//оператор должен возвращать ссылку на поток, так как cout << 0 << 0;
//это вызов operator<<(operator<<(cout, 0), 0)
ostream& operator<<(ostream& ost, const Duration& duration){
    ost << setfill('0');
    ost << setw(2) << duration.mm << ":" << setw(2) << duration.ss;
    return ost;
}

istream& operator>>(istream& ist, Duration& duration){
    ist >> duration.mm;
    ist.ignore(1);
    ist >> duration.ss;
    return ist;
}

Duration operator+(const Duration& duration_1, const Duration& duration_2){
    return Duration{duration_1.mm + duration_2.mm, duration_1.ss + duration_2.ss};
}

int main(){
    stringstream ss("0311;42");
    Duration duration;
    ss >> duration;
    cout << duration;

    /*
    cout << ReadDuration(ss);
    cout << ENDLINE;
    PrintDuration(cout, ReadDuration(ss));
*/
}