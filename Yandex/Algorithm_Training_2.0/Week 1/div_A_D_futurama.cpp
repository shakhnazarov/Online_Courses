#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>

using namespace std;

void Swap(map<int, int>& minds){

}

int main(){
    int N, M;
    cin >> N >> M;
    map<int, int> minds;
    set<set<int>> swaps;

    int num1, num2;
    for(int i=0; i<M; ++i){
        cin >> num1 >> num2;
        swaps.insert({num1, num2});
        minds[num1] = num2;
    }

    for (const auto& item : minds){
        if (item.first == item.second){
            minds.erase(item.first);
            continue;
        }
        if(item.second == minds[item.second] && swaps.count({item.second, minds[item.second] })==0){

        }

    }




    return 0;
}