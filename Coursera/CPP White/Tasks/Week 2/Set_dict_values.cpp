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

set<string> BuildMapValuesSet(const map<int, string>& m) {
    set<string> setty;
    for (const auto & value : m) {
        setty.insert(value.second);
    }
    return setty;
}