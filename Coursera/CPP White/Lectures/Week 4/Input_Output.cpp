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

void ReadAll (const string& path){
    ifstream input(path);

    if(input){
        string line;
        while (getline(input, line)){
            cout << line << ENDLINE;
            input.ignore(1); //игнорируем один символ перед концом строки (???)
        }
  }
}


int main(){

    //можем заранее задефайнить путь
    const string path = "D:/Programming/CPP/Coursera/Test_out10.txt";


    //джае если файла нет, не будет ошибки


    //Можем вписывать в файл
    ofstream output(path, ios::app); //мод чтобы не заменять содержимое файла
    output << "proverka" << ENDLINE;
    ReadAll(path);
/*
    //Можно проверить открылся ли поток
    if (input.is_open()){ //потоки приводятся к типу бул
        while(getline(input, line, 'a')){ // ожем добавить делиметер
            cout << line << ENDLINE;
            input >> line; //можем считывать из потока
            cout << line << ENDLINE;
        }
        cout << "done" << ENDLINE;
    } else {
        cout << "How" << ENDLINE;
    }

    //Можно отдельно вызывать каждую строку

    getline(input, line);
    cout<< line << ENDLINE;
    getline(input, line);
    cout<< line << ENDLINE;

    //или сразу всё считать из потока, так как есть работа с bool значениями
    while(getline(input, line)){
        cout << line << ENDLINE;
    }

*/


    return 0;
}