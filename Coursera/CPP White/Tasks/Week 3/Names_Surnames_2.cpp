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

    string GetFullNameWithHistory(int year) {
        if((year < second_name_map.begin() -> first) && (year < first_name_map.begin() -> first) || (second_name_map.empty() && first_name_map.empty())
           || second_name_map.empty() && year < first_name_map.begin() -> first || first_name_map.empty() && year < second_name_map.begin() -> first){
            return "Incognito";
        } else if (year < second_name_map.begin() -> first || second_name_map.empty()) {
            string hist_name = NameForPrint(GetFirstNameHistory(year));
            return (hist_name.empty()) ? GetFirstNameByYear(year) + " with unknown last name" : GetFirstNameByYear(year) + " " + hist_name + " with unknown last name";
        } else if (year < first_name_map.begin() -> first || first_name_map.empty()){
            string hist_name = NameForPrint(GetSecondNameHistory(year));
            return (hist_name.empty()) ? GetSecondNameByYear(year) + " with unknown first name" : GetSecondNameByYear(year) + " " + hist_name + " with unknown first name";
        } else {
            string hist_first_name = NameForPrint(GetFirstNameHistory(year)), hist_second_name = NameForPrint(GetSecondNameHistory(year));
            if (hist_first_name.empty() && hist_second_name.empty()){
                return GetFirstNameByYear(year) + " " + GetSecondNameByYear(year);
            } else if (hist_first_name.empty()){
                return GetFirstNameByYear(year) + " " + GetSecondNameByYear(year) + " " + hist_second_name;
            } else if (hist_second_name.empty()){
                return GetFirstNameByYear(year) + " " + hist_first_name + " " + GetSecondNameByYear(year);
            } else {
                return GetFirstNameByYear(year) + " " + hist_first_name + " " + GetSecondNameByYear(year) + " " + hist_second_name;
            }
        }
    }


public:

    string NameForPrint(const vector<string>& vec) {
        int N = vec.size();
        if (N == 0){
            return "";
        }
        string name_history = "(";
        for (int i = N-1; i >-1; --i){
            name_history += (vec[i] + ", ");
        }
        name_history.pop_back();
        name_history.pop_back();
        name_history+=")";
        return name_history;
    }

private:
    vector<string> GetFirstNameHistory (const int& year) {
        vector<string> names = {first_name_map.begin() -> second};
        for (auto & it : first_name_map) {
            if (year >= it.first) {
                if (names.back() == it.second) {
                    continue;
                }
                names.push_back(it.second);
            } else {
                names.pop_back();
                return names;
            }

        }
        names.pop_back();
        return names;
    }

    vector<string> GetSecondNameHistory (const int& year) {
        vector<string> names = {second_name_map.begin() -> second};
        for (auto & it : second_name_map) {
            if (year >= it.first) {
                if (names.back() == it.second) {
                    continue;
                }
                names.push_back(it.second);
            } else {
                names.pop_back();
                return names;
            }
        }
        names.pop_back();
        return names;
    }

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
    map<int, vector<string>> first_name_map_history;
    map<int, vector<string>> second_name_map_history;
};

int main() {
    {
        Person person;
        person.ChangeFirstName(1, "first");
        person.ChangeFirstName(2, "first2");
        person.ChangeFirstName(3, "first3");
        person.ChangeFirstName(4, "first");
        person.ChangeFirstName(5, "first5");
        std::cout << person.GetFullName(5) << '\n';
        std::cout << person.GetFullNameWithHistory(5) << '\n';

    }
    return 0;
}

