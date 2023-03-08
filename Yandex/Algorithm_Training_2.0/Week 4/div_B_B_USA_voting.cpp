#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#define ENDLINE "\n"

using namespace std;

int main(){
    int num;
    string input_string, candidate;
    map<string, int> votes;
    while(cin >> candidate >> num){
        if(votes.count(candidate)==0){
            votes[candidate]=0;
        }
        votes[candidate]+=num;
    }

    for (const auto& item : votes){
        cout << item.first << " " << item.second << ENDLINE;
    }

    return 0;
}