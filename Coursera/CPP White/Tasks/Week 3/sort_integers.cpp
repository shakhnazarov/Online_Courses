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

void Print(const vector<int>& vec){
    for (auto& item : vec){
        cout << item << " ";
    }
}

int main() {
    int N;
    int num_inp;

    cin >> N;
    vector<int> nums(N);
    for (int& num : nums){
        cin >> num_inp;
        num = num_inp;
    }
    sort(nums.begin(), nums.end(), [](int x, int y){return abs(x) < abs(y);});
    Print(nums);
    return 0;
}
