#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string a;
    cin >> a;
    int k = -2;
    for (int i = 0; i < a.length(); ++i ) {
        if (a[i] == 'f') {
            ++k;
            if (k == 0) {
                k = i;
                break;
            }
        }
    }
    cout << k;

    return 0;
}