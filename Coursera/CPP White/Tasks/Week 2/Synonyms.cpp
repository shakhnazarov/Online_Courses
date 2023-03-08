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

void ADD(map<string, set<string>>& mappy){
    string word1, word2;
    cin >> word1 >> word2;
    mappy[word1].insert(word2);
    mappy[word2].insert(word1);

}

void COUNT(map<string, set<string>>& mappy){
    string word;
    cin >> word;
//    set<string> syn_check;
 //   syn_check.insert(mappy[word].begin(), mappy[word].end());
//
//    for (const auto& item : mappy){
//        if(item.second.count(word)){
 //           syn_check.insert(item.first);
 //       }
 //   }
    cout << mappy[word].size() << ENDLINE;

}

//здесь мы делаем копию чтобы не понасоздавать лшних пар, но можно наверное лучше
void CHECK(map<string, set<string>>& mappy){
    string word1, word2;
    cin >> word1 >> word2;
    if (mappy[word1].count(word2)){
        cout << "YES" << ENDLINE;
    } else {
        cout << "NO" << ENDLINE;
    }
}

int main() {
    int Q;
    string com;
    map<string, set<string>> syn;
    cin >> Q;
    for( int i = 0; i<Q; ++i) {
        cin >> com;
        if (com == "ADD") {
            ADD(syn);
        } else if (com == "COUNT") {
            COUNT(syn);
        } else {
            CHECK(syn);
        }
    }
}