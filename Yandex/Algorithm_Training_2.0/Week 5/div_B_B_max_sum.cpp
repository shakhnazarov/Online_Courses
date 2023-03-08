#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <unordered_set>
#include <vector>
#define ENDLINE "\n"

using namespace std;

int main(){

    int n;
    cin >> n;
    vector<int> nums(n);
    vector<long long int> prefix_sum = {0};
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
        prefix_sum.push_back(prefix_sum[i]+nums[i]);
    }

    auto it_max = max_element(prefix_sum.begin(), prefix_sum.end()),
    it_min = min_element(prefix_sum.begin(), prefix_sum.end());

    long long int ans;
    if(it_max >= it_min){
        ans = *it_max - *it_min;
    } else {
        ans = max(
                *it_max - *min_element(prefix_sum.begin(), it_max),
                *max_element(it_min, prefix_sum.end()) - *it_min
                );
    }

    if(ans == 0){
        ans = *max_element(nums.begin(), nums.end());
    }
    cout << ans;
    return 0;
}