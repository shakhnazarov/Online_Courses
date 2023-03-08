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

void ReadAll(const string& path){
    ifstream input(path);
    if(input){
        string line;
        while(getline(input, line)){
            cout << line << ENDLINE;
        }
    }
}


int main(){
    const string path = "input.txt";
    ReadAll(path);

    return 0;
}