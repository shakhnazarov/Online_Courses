#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    if (B == 0){
        cout << "Impossible";
    } else {
        cout << A/B;
    }


    return 0;
}