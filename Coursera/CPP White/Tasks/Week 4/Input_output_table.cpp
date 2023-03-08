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

void ReadAllWrite(const string& path_input){
    ifstream input(path_input);
    if(input){
        int N = 0, M=0;
        input >> N;
        input >> M;
        string line, temp, word;
        cout << setfill(' ') << right;

        input.ignore(20000, '\n');
        while (input >> line){

            stringstream s(line);

            while (getline(s,word, ',')){
                cout << setw(10) << word;
                if(s.peek()!= EOF){
                    cout << " ";
                }
            }
            if(input.peek()!= EOF){
                cout << ENDLINE;
            }

        }
        /*
        for (int j =0; j<N; ++j){
            for (int i =0; i<M; ++i){
                getline(input, line, ',');
                cout << setw(10) << line;
            }
            input.ignore(20000, '\n');
            cout << ENDLINE;
        }
         */
    } else {
        cout <<"op";
    }
}


int main(){
    const string path_input = "input.txt";
    const string path_output = "output.txt";
    //const string path_input = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/input.txt";
    //const string path_output = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/output.txt";
    ReadAllWrite(path_input);

    return 0;
}