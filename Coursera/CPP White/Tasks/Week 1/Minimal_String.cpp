#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string a, b, c;
    cin >> a >> b >> c;
    if (a <= b) {
        if ( c <= a) {
            cout << c;
        }
        else {
            cout << a;
        }
    } else {
        if ( c <= b) {
            cout << c;
        }
        else {
            cout << b;
        }
    }

    return 0;
}