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

void Print(const vector<string>& vec){
    for (auto& item : vec){
        cout << item << " ";
    }
}

int main() {
    int N;
    string str_inp;
    cin >> N;
    vector<string> nums(N);
    for (auto& str : nums){
        cin >> str_inp;
        str = str_inp;
    }

    sort(nums.begin(), nums.end(), [](string x, string y){
        transform(x.begin(), x.end(), x.begin(), [](char c){ return tolower(c);});
        transform(y.begin(), y.end(), y.begin(), [](char c){ return tolower(c);});
        return x < y;
    });
    Print(nums);
    return 0;
}
