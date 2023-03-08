#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int main(){
    int N, num, K;
    cin >> N >> K;
    vector<long int> nums;
    for (int i = 0; i<N; ++i){
        cin >> num;
        nums.push_back(num);
    }


        cout << abs(-*min_element(nums.begin(), nums.end()) + *max_element(nums.begin(), nums.end()));
    return 0;
}