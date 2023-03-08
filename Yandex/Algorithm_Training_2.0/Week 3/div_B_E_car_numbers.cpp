#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#include <map>

#define ENDLINE '\n'
using namespace std;

/// не понимаю какую структуру лучш использовать чтобы preserve order вывода
int main(){
    int M=0;
    cin >> M;
    string inp;
    unordered_set<string> witnesses;
    for (int i = 0; i < M; ++i) {
        cin >> inp;
        witnesses.insert(inp);

    }

    int N=0;
    cin >> N;
    vector<string> numbers;

    for (int i = 0; i < N; ++i) {
        cin >> inp;
        numbers.push_back(inp);
    }

    map<int, vector<string>> ans;
    unordered_set<char> num_chars;
    bool has_not_seen=false;
    int num_wit=0;

    for(const auto& item : numbers){
        for(const auto& let : item){
            num_chars.insert(let);
        }
        for (const auto & item1 : witnesses) {
            for(const auto& let1 : item1){
                if(num_chars.count(let1)==0){
                    has_not_seen = true;
                    break;
                }
            }
            if(!has_not_seen){
                num_wit++;
            }
            has_not_seen=false;
        }

        ans[num_wit].push_back(item);
        num_wit=0;
        num_chars.clear();
    }

    for(const auto& item : ans.rbegin() -> second){
        cout << item << ENDLINE;
    }

    return 0;
}