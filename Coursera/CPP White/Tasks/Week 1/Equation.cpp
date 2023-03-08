#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main() {
    double A, B, C;
    cin >> A >> B >> C;
    double D = B*B - 4*A*C;
    if (A != 0) {
        if (D < 0) {
            cout << "";
        } else if (D == 0) {
            cout << -B/(2*A);
        } else {
            cout << (-B - sqrt(D))/(2*A) << " " << (-B + sqrt(D))/(2*A);
        }
    } else {
        if (B == 0) {
            cout << "";
        }
        else if (C == 0) {
            cout << 0;
        } else {
            cout << -C/B;
        }
    }

    return 0;
}