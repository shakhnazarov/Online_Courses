#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;


class Person {
public:
    void ChangeFirstName(int year, const string& first_name) {
        first_name_map[year] = first_name;
    }
    void ChangeLastName(int year, const string& last_name) {
        second_name_map[year] = last_name;
    }
    string GetFullName(int year) {
        //зайюзали поинтеры, ибо вначале мап отсортирован
        if((year < second_name_map.begin() -> first) && (year < first_name_map.begin() -> first) || (second_name_map.empty() && first_name_map.empty())
        || second_name_map.empty() && year < first_name_map.begin() -> first || first_name_map.empty() && year < second_name_map.begin() -> first){
            return "Incognito";
        } else if (year < second_name_map.begin() -> first || second_name_map.empty()) {
            return GetFirstNameByYear(year) + " with unknown last name";
        } else if (year < first_name_map.begin() -> first || first_name_map.empty()){
            return GetSecondNameByYear(year) + " with unknown first name";
        } else {
            return GetFirstNameByYear(year) + " " + GetSecondNameByYear(year);
        }
    }


private:
    string GetFirstNameByYear(int year){
        if(year >= first_name_map.rbegin() -> first){
            return first_name_map.rbegin() -> second;
        }
        string name;
        for (auto & it : first_name_map){
            if (year >= it.first){
                name = it.second;
            } else {
                return name;
            }

        }
    }

    string GetSecondNameByYear(int year){
        if(year >= second_name_map.rbegin() -> first){
            return second_name_map.rbegin() -> second;
        }
        string name;
        for (auto & it : second_name_map){
            if (year >= it.first){
                name = it.second;
            } else {
                return name;
            }

        }
    }


private:

    //так то было бы хорошо создать вектор сразу с фиксированной длинной
    // для этого нужно wrap и создать новый struct
    //map<int, vector<string>> association;

    map<int, string> first_name_map;
    map<int, string> second_name_map;
};

int main() {
    Person person;

    cout << person.GetFullName(2000) << endl;
    person.ChangeLastName(1968, "1968_2nd");
    person.ChangeLastName(1967, "1967_2nd");
    person.ChangeLastName(1965, "1965_2nd");
    person.ChangeLastName(1966, "1966_2nd");

    for (int year : {1900, 1920, 1950, 1965, 1966, 1967, 1968}) {
        cout << person.GetFullName(year) << endl;
    }

    person.ChangeFirstName(1920, "1920_1st");
    person.ChangeFirstName(1900, "1900_1st");
    person.ChangeFirstName(1965, "1965_1st");
    person.ChangeFirstName(1950, "1950_1st");

    for (int year : {1900, 1920, 1950, 1965, 1966, 1967, 1968}) {
        cout << person.GetFullName(year) << endl;
    }
    return 0;
}