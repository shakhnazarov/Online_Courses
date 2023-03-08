#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int main(){
    int num = 0;
    vector<int> nums, ind_homes, ind_shops;
    for(int i =0; i<10; ++i){
        cin >> num;
        nums.push_back(num);
        if(num==2){
            ind_shops.push_back(i);
        }
        if(num == 1){
            ind_homes.push_back(i);
        }
    }
    int d = 11;
    set<int> dists;
    for(auto item : ind_homes){
        d=11;
        for(auto item1 : ind_shops){
            d = min(d, abs(item-item1));
        }
        dists.insert(d);
    }
    cout << *dists.rbegin();

    //пустая последов или один симовл
    return 0;
}