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
    int N, K;
    cin >> N >> K;

    int initial, regularity;
    unordered_set<int> days;
    for (int i = 0; i < K; ++i) {
        cin >> initial >> regularity;
        for(int j =initial; j<N+1; j+=regularity){
            if(!(j%7==6 || j%7==0)){
                days.insert(j);
            }
        }
    }

    cout << days.size();



    return 0;
}