#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int N, rem;
    string bin;
    cin >> N;
    while (N !=0) {
        bin +=  to_string(N%2);
        N /= 2;
    }
    for (int i = bin.length() - 1; i != -1; --i){
        cout << bin[i];
    }
    return 0;
}