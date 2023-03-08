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



struct Student{
    string name;
    string surname;
    string day;
    string month;
    string year;
};

void ReadAllStudents(const string& path_input, const string& path_output, vector<Student>& students) {
    ifstream input(path_input);
    if (input) {
        int N;
        input >> N;
        string line, part;
        vector<string> student_values;
        input.ignore(100000, '\n');
        for (int i = 0; i < N; ++i) {
            getline(input, line);
            stringstream s(line);
            for (int j = 0; j < 5; ++j) {
                getline(s, part, ' ');
                student_values.push_back(part);
            }
            students.push_back({student_values[0], student_values[1],
                                student_values[2], student_values[3],
                                student_values[4]});
            student_values.clear();
        }


        ofstream output(path_output, ios::app);

        int M, K;
        string com;
        input >> M;
        input.ignore(1000000, '\n');
        for (int i = 0; i < M; ++i) {
            getline(input, line);
            stringstream s(line);

            //читаем команду
            getline(s, com, ' ');
            s >> K;

            if (com == "name"){
                output << students[K-1].name << " " << students[K-1].surname << ENDLINE;
            } else if(com == "date"){
                output << students[K-1].day << "." << students[K-1].month << "." << students[K-1].year << ENDLINE;
            }else{
                output << "bad request" << ENDLINE;
            }

        }
    }
}

void WriteAllStudents(const string& path_output, vector<Student>& students){
    ofstream output(path_output, ios::app);
    int M=0, K=0;
    cin >> M;
    string com;
    for (int i =0; i<M; ++i){
        cin >> com;
        cin >> K;
        if (com == "name"){
            output << students[K-1].name << " " << students[K-1].surname << ENDLINE;
        } else if(com == "date"){
            output << students[K-1].day << "." << students[K-1].month << "." << students[K-1].year << ENDLINE;
        }else{
            output << "bad request" << ENDLINE;
        }
    }
}

int main() {
    //const string path_input = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/input_students.txt";
    const string path_input = "input.txt";
    //const string path_output = "D:/Programming/CPP/Coursera/Tasks/White/Week 4/output_students.txt";
    const string path_output = "output.txt";
    vector<Student> students;

    ReadAllStudents(path_input, path_output, students);
    return 0;
}