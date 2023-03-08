#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#define ENDLINE "\n"

using namespace std;

int main(){

    string input_string, candidate;
    map<string, int> votes;
    while(cin >> candidate){
        //if(candidate=="q"){
          //  break;
        //}
        if(votes.count(candidate)==0){
            votes[candidate]=0;
        }
        votes[candidate]++;
    }

    map<int, set<string>> ans;
    for (const auto& item : votes){
        ans[item.second].insert(item.first);
    }
    for (auto it=ans.rbegin(); it != ans.rend(); it++){
        for(const auto& word : (it -> second)){
            cout << word << ENDLINE;
        }
    }

    return 0;
}