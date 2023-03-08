#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    int L, num, K;
    cin >> L >> K;
    vector<int> nums;
    for(int i = 0; i<K; ++i){
        cin >> num;
        nums.push_back(num);
    }
    if(L==1){
        cout << 0;
        return 0;
    }

    int size = L/2, ind;
    for(int i = 0; i<K; ++i){
        if(nums[i] >= size){
            ind = i;
            break;
        }
    }
    if(nums[ind]==L/2 && L%2==1){
        cout << nums[ind];
    } else{
        cout << nums[ind-1] << " " << nums[ind];
    }
    return 0;
}