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

    int n, q;
    cin >> n >> q;

    vector<int> nums(n);
    vector<long long int> prefix_sum = {0};
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
        prefix_sum.push_back(prefix_sum[i]+nums[i]);
    }

    int l, r;
    for (int i = 0; i < q; ++i) {
        cin >> l >> r;
        cout << prefix_sum[r] - prefix_sum[l-1] << ENDLINE;
    }
    return 0;
}