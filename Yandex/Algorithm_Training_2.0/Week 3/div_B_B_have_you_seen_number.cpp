#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#define ENDLINE '\n'
using namespace std;

int main(){
    int num, count=0;
    set<int> nums;
    while (cin >> num){
        if(nums.count(num)==1){
            cout << "YES" << ENDLINE;
        }else{
            cout << "NO" << ENDLINE;
            nums.insert(num);
        }
    }

    return 0;
}