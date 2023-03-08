#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool   IsPalindrom (string num) {
    string rev;
    for (int i = num.length()-1; i != -1; --i) {
        rev += num[i];
    }
    return rev == num;
}

bool IsPalindromSolution(string s) {
    // Замечание: более правильным было бы использовать здесь тип size_t вместо int
    // О причинах Вы узнаете на Жёлтом поясе
    for (int i = 0; i < s.size() / 2; ++i) {
        if (s[i] != s[s.size() - i - 1]) {
            return false;
        }
    }
    return true;
}


int main() {
    string a;
    cin >> a;
    cout <<   IsPalindrom(a);
    return 0;
}