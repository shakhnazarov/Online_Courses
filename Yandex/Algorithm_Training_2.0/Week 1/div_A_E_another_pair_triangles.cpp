#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int P;
    cin >> P;

    if (P==4){
        cout << -1;
        return 0;
    }

    if(P%3==0 || P%3==1){
        cout << P/3 + P%3 << " " << P/3 << " " << P/3 << endl;
    } else{
        cout << P/3 + 1 << " " << P/3 + 1 << " " << P/3 << endl;
    }

    if(P%2==1){
        cout << P/2 << " " << P/2 << " " << 1;
    } else {
        cout << P/2 - 1 << " " <<  P/2 - 1 << " " << 2;
    }

    return 0;
}