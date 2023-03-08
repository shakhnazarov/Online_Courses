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

void EnsureEqual(const string& left, const string& right){
    if(left!=right){
        stringstream ss;
        ss << left << " != " << right;
        throw runtime_error(ss.str());
    }
};

int main() {
    try {
        EnsureEqual("C++ White", "C++ White");
        EnsureEqual("C++ White", "C++ Yellow");
    } catch (runtime_error& e) {
        cout << e.what() << endl;
    }
    return 0;
}