#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    int num = 0, N, sum = 0;
    cin >> N;
    vector<int> nums;
    for(int i =0; i<N; ++i){
        cin >> num;
        nums.push_back(num);
        sum+= num;
    }

    int max=nums[0];
    for(int i =1; i<N; ++i){
        if(nums[i]>max){
            max = nums[i];
        }
    }

    cout << sum - max;
    //пустая последов или один симовл
    return 0;
}