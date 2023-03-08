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

int main() {
    int N;
    string word;
    set<string> words;
    cin >> N;
    for (int i = 0; i<N; ++i) {
        cin >> word;
        words.insert(word);
    }
    cout << words.size();

}