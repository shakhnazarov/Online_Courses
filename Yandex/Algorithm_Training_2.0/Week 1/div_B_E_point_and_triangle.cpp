#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int d, x1,x2;
    cin >> d >> x1 >> x2;

    if (x1 >= 0 && x2>= 0 && (x2 <= d - x1) && x1 <=d){
        cout << 0;
    } else{
        int A = sqrt(x1*x1 + x2*x2), B = sqrt((x1-d)*(x1-d) + x2*x2), C = sqrt(x1*x1 + (x2-d)*(x2-d));
        int p = min(A, min(B,C));
        if(p==A){
            cout << 1;
        } else if (p==B){
            cout << 2;
        } else {
            cout << 3;
        }

    }

    return 0;
}