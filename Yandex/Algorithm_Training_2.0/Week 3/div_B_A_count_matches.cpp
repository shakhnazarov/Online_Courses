#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    int num, count=0;
    set<int> nums;
    while (cin >> num){
        if(nums.count(num)==1){
            count++;
        }else{

            nums.insert(num);
        }
    }

    cout << count;
    return 0;
}