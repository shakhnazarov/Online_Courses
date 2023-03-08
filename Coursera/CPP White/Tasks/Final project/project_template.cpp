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

class Date {
public:
    Date(){
        year = 0;
        month = 0;
        day = 0;
    }
    Date(const int& year, const int& month, const int& day){
        if(month > 12 || month < 1){
            throw invalid_argument("Month value is invalid: " + to_string(month));
        }
        if(day < 1 || day > 31){
            throw invalid_argument("Day value is invalid: " + to_string(day));
        }
        this -> year = year;
        this -> month = month;

        this -> day = day;
    }
  int GetYear() const{
      return year;
  };
  int GetMonth() const{
      return month;
  };
  int GetDay() const {
      return day;
  };

private:
    int year;
    int month;
    int day;
};

struct Event{
    string event;
};

//перегружаем операторы ввывода для Date и Event
ostream& operator<<(ostream& ostream1, const Event& event1){
    ostream1 << event1.event;
    return ostream1;
}

istream& operator>>(istream& istream1, Event& event1){
    istream1 >> event1.event;
    return istream1;
}

bool operator<(const Event& lhs, const Event& rhs){
    return (lhs.event < rhs.event);
}

ostream& operator<<(ostream& ostream1, const Date& date1){
    //TO-DO непонятно по отрицательным датам - сколько максимальнное число
    ostream1 << setw(4) << setfill('0') << right << date1.GetYear()  << "-" << setw(2) << date1.GetMonth()
    << "-" << setw(2) << date1.GetDay();
    return ostream1;
}

istream& operator>>(istream& istream1, Date& date){
    int year, month, day;
    string input_string;
    /* //првоерка не работает если закинут +0 или -0 в месяц или день
    istream1 >> input_string;
    stringstream s(input_string);
    char elem = s.peek();
    s >> year;
    if(year == 0 && elem != '0'){
        throw invalid_argument("Wrong date format: " + input_string);
    }
    if(s.peek() == '-'){
        s.ignore(1);
        char elem = s.peek();
        s >> month;
        if(month == 0 && elem != '0'){
            throw invalid_argument("Wrong date format: " + input_string);
        }
        if(s.peek() == '-'){
            s.ignore(1);
            char elem = s.peek();
            s >> day;
            if(day == 0 && elem != '0'){
                throw invalid_argument("Wrong date format: " + input_string);
            }

        }
    }
*/
    istream1 >> input_string;
    int num_plus = 0, num_minus = 0, total_num_minus = 0, N = input_string.size();
    for(int i = 0; i < N - 1; ++i){
        if(isalpha(input_string[i])){
            throw invalid_argument("Wrong date format: " + input_string);
        }
        if (ispunct(input_string[i]) && input_string[i] != '-' && input_string[i] != '+'){
            throw invalid_argument("Wrong date format: " + input_string);
        }
        if(input_string[i] == '+'){
            ++num_plus;
            if(num_plus == 2 || input_string[i+1] == '-'){
                throw invalid_argument("Wrong date format: " + input_string);
            }
        } else {
            num_plus = 0;
        }
        if (input_string[i] == '-'){
            ++num_minus;
            ++ total_num_minus;
            if(num_minus == 3){
                throw invalid_argument("Wrong date format: " + input_string);
            }
        } else {
            num_minus = 0;
        }
    }
    if(!isdigit(input_string.back())){
        throw invalid_argument("Wrong date format: " + input_string);
    }
    if(!(input_string[0] == '+' || isdigit(input_string[0]))){
        throw invalid_argument("Wrong date format: " + input_string);
    }
    if(total_num_minus <2){
        throw invalid_argument("Wrong date format: " + input_string);
    }

    stringstream s(input_string);
    s >> year;
    s.ignore(1);
    s >> month;
    s.ignore(1);
    s >> day;
    date = {year, month, day};

    return istream1;
}

bool operator<(const Date& lhs, const Date& rhs){
    if(lhs.GetYear() < rhs.GetYear()){
        return true;
    } else if (lhs.GetYear() > rhs.GetYear()){
        return false;
    } else{
        if(lhs.GetMonth() < rhs.GetMonth()){
            return true;
        } else if (lhs.GetMonth() > rhs.GetMonth()){
            return false;
        } else{
            if (lhs.GetDay() < rhs.GetDay()){
                return true;
            } else {
                return false;
            }
        }
    }
}


// Создаём класс Database
class Database {
public:
     void AddEvent(const Date& date, const Event& event){
        events[date].insert(event);
    }

    void DeleteEvent(const Date& date, const Event& event){
        if (events.count(date) != 0){
            if (events[date].count(event) != 0) {
                events[date].erase(event);
                cout << "Deleted successfully" << ENDLINE;
            } else {
                cout << "Event not found" << ENDLINE;
            }
        } else {
            cout << "Event not found" << ENDLINE;
        }

    }

    void DeleteDate(const Date& date){
        int num_of_events = events[date].size();
        events.erase(date);
        cout << "Deleted " << num_of_events << " events" << ENDLINE;

    }

    void FindEvents(const Date& date) {
        if(events.count(date) != 0){
            for (const auto& item : events[date]){
                cout << item << ENDLINE;
            }
        }
    }


    void Print() const{
        //TO-DO не знаю в каком порядке будут даты выдаваться
        for (const auto& item : events){
            for (const auto& event : item.second){
                cout << item.first << " " << event << ENDLINE;
            }
        }
    }

private:
    map<Date, set<Event>> events;
};

int main() {
  Database db;
  string command;
  string com;
  Date date;
  Event event;
    while (getline(cin, command)) {
        stringstream s(command);

        if (s.peek() != EOF){
            s >> com;
        }
        try {
            if(com == "Add"){
                s >> date;
                s >> event;
                db.AddEvent(date, event);

            } else if (com == "Find"){
                s >> date;
                db.FindEvents(date);
            } else if(com == "Del"){
                s >> date;
                if(s.peek() != EOF){
                    s >> event;
                    db.DeleteEvent(date, event);
                } else{
                    db.DeleteDate(date);
                }
            } else if(com == "Print"){
                db.Print();
            } else if(com != ""){
                cout << "Unknown command: " << com << ENDLINE;
            }

        } catch (exception& e){
            cout << e.what() << ENDLINE;
        }
    com = "";
    }

  return 0;
}