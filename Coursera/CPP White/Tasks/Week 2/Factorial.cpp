#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int Factorial (int N) {
    if (N > 0) {
        int fact = 1;
        for (int i = 1; i <= N; ++i) {
            fact *= i;
        }
        return fact;
    } else {
        return 1;
    }
}

int main() {

    return 0;
}