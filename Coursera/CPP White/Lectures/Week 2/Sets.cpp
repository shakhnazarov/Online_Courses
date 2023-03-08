#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

void PrintMap(const set<string>& setty) {
    for (auto item: setty) {
        cout << item << ENDLINE;
    }
}

int main() {
    set<string> yet_another;
    yet_another.insert("stringa");
    yet_another.insert("vtoraya_stringa");
    vector<string> s = {"Alla", "ONA"};
    yet_another.insert(s.begin(), s.end());
    PrintMap(yet_another);
    return 0;
}