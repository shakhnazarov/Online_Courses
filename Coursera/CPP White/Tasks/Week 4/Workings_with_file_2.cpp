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

void ReadAllWrite(const string& path_input, const string& path_output){
    ifstream input(path_input);
    if(input){
        string line;
        ofstream output(path_output);
        while(getline(input, line)){
            output << line;
            output << ENDLINE;
        }

    }
}


int main(){
    const string path_input = "input.txt";
    const string path_output = "output.txt";
    //const string path_input = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/input.txt";
    //const string path_output = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/output.txt";

    ReadAllWrite(path_input, path_output);

    return 0;
}