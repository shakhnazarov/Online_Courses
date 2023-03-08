#include <iostream>
#include <algorithm>
using namespace std;

int main(){

    int a, b, c;
    cin >> a >> b >> c;
    if(a > 12 || b > 12 || a==b){
        cout << 1;
    } else{
        cout << 0;
    }
}