#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        nums[i] = -1 * stoi(s);
    }

    for (int i = 0; i < m; i++) {
        int q;
        cin >> q;
        int res = lower_bound(nums.begin(), nums.end(), -1*q) - nums.begin() + 1;
        if (res <= n) {
            cout << res << endl;
        } else {
            cout << "NO SOLUTION" << endl;
        }
    }
    return 0;
}