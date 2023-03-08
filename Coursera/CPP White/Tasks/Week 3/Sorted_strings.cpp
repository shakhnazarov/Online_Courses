#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

class SortedStrings {
public:
    void AddString(const string& s) {
        strings.push_back(s);
        SortStrings();

    }
    vector<string> GetSortedStrings() {
        return strings;
    }

private:
    void SortStrings(){
        sort(strings.begin(), strings.end());
    }
private:
    vector<string> strings;
};