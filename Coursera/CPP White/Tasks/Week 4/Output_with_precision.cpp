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

void ReadAllPrecision(const string& path_input){
    ifstream input(path_input);

    double line;
    cout << fixed << setprecision(3);
    while(input >> line){
        cout << line << ENDLINE;
    }
}


int main(){
    //const string path_input = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/input.txt";
    const string path_input = "input.txt";
    const string path_output = "output.txt";
    ReadAllPrecision(path_input);

    return 0;
}