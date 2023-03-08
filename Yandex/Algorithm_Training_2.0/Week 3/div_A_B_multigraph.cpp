#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#include <fstream>
#include <sstream>
#define ENDLINE '\n'
using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    set<set<int>> ans;
    int first, second;
    for (int i =0;  i < m; ++i){
        cin >> first >> second;
        if(first != second){
            ans.insert({first, second});
        }
    }

    set<int> nodes;
    for (const auto& item : ans){
        nodes.insert(*item.begin());
        nodes.insert(*item.rbegin());
    }

    cout << *nodes.rbegin() << " " << ans.size() << ENDLINE;
    for (const auto& item : ans){
        cout << *item.begin() << " " << *item.rbegin() << ENDLINE;
    }
    return 0;
}