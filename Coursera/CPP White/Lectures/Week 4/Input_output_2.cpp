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


int main(){

    vector<string> str = {"am", "asd", "asfds"};
    vector<double> nums = {1, 123123, 0.0000044};


    for (const auto& val : str){
        cout << setw(20) << val << " ";
    }
    cout << ENDLINE;
    for (const auto& val : nums){
        cout << val << " ";
    }
    cout << ENDLINE;
    cout << setfill('.') << left; //символсы начинаются слева и зполняются точками
    cout << fixed << setprecision(11); //фиксированное количество знаков после запятой
    for (const auto& val : nums){
        cout << setw(20) << val << " "; //настраиваем фиксированную ширину столбца
    }
    return 0;
}