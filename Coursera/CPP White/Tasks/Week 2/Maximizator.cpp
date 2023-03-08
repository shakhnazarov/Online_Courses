#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void UpdateIfGreater (int first, int& second) {
    if (first > second) {
        second = first;
    }
}

int main() {
    int x, y;
    cin >> x >> y;
    UpdateIfGreater(5, y);
    cout << x << y;
    return 0;
}