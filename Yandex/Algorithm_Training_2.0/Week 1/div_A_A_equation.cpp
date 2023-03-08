#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if(c*double((-b))/a + d == 0 || (a==0 && b!=0)){
        cout << "NO";
    } else if(a==0 && b==0){
        cout << "INF";
    } else if(double(-b)/a == -b/a){
        cout << -b/a;
    } else {
        cout << "NO";
    }

    return 0;
}