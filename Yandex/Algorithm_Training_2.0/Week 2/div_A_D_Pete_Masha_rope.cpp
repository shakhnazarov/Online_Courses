#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int main(){
    int N, num;
    cin >> N;
    vector<int> nums;
    for (int i = 0; i<N; ++i){
        cin >> num;
        nums.push_back(num);
    }
    sort(nums.begin(), nums.end());
    int sum = 0;
    for (auto it = nums.begin(); it != --nums.end(); ++it){
        sum += *it;
    }

    if(sum<*nums.rbegin()){
        cout << *nums.rbegin() - sum;
    } else{
        cout << *nums.rbegin() + sum;
    }
    return 0;
}