#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

string BuildCharCounters(string& first, string& second) {
    map<char,int> counter1, counter2;
    for (auto& let : first) {
        ++counter1[let];
    }
    for (auto& let : second) {
        ++counter2[let];
    }
    //ternary operator
    return (counter1 == counter2) ? "YES\n" : "NO\n";
}

int main() {
    int N;
    cin >> N;
    string word1, word2;
    for (int i = 0; i<N; ++i){
        cin >> word1 >> word2;
        cout << BuildCharCounters(word1, word2);
    }
    return 0;
}