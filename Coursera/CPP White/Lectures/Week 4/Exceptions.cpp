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
#include <numeric>
#include <chrono> //можем замерять работу программы
#define ENDLINE "\n"


using namespace std;

struct Date{
    int day;
    int month;
    int year;
};

void CheckNextSymbol(stringstream& s) {
    if(s.peek()!= '/'){
        stringstream ss;
        ss << "Expected / but got " << char(s.peek());
        throw runtime_error(ss.str());//exception(ss.str());
    }
}

Date ParseDate(const string& string1){
    try {
        stringstream s(string1);
        Date date;
        s >> date.day;
        CheckNextSymbol(s);
        s >> date.month;
        CheckNextSymbol(s);
        s >> date.year;
        return date;
    } catch (exception& exception){
        cout << exception.what();
    }
}


int main() {
    string s = "123.123";
    ParseDate(s);



}