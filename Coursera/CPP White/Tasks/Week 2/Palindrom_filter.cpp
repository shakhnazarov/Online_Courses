#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;



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

vector<string> PalindromFilter (vector<string> words, int minLength) {
    vector<string> palindroms;
    for (auto word : words){
        if (word.size()>= minLength){
            if(IsPalindromSolution(word)){
                palindroms.push_back(word);
            }
        }
    }
    return palindroms;
}

int main() {

}