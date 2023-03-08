#include <vector>
#include <iostream>
#include <string>
using namespace std;

int euclid_1 (int a, int b) {
    int c = max(a,b);
    int d = min(a, b);
    while (max(c,d) % min(c,d) != 0) {
        if (max(c,d) == c) {
            c %= d;
        } else {
            d %= c;
        }
    }
    return min(c, d);
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << euclid_1(a, b);


    return 0;
}