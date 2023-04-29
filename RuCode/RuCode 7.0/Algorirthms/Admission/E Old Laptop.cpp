#include <iostream>
#include <vector>

using namespace std;

int main() {
    int X;
    cin >> X;

    vector<bool> nums(X+1, true);
    nums[0] = false;
    nums[1] = false;

    for (int i = 2; i <= X; i++) {
        if (nums[i] == true) {
            int k = 2;
            while (i * k <= X) {
                nums[i*k] = false;
                k += 1;
            }
        }
    }

    int count = 0;
    for (bool val : nums) {
        if (val == true) {
            count++;
        }
    }
    cout << count << endl;

    return 0;
}