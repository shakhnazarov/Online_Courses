#include <iostream>
#include <algorithm>
using namespace std;

int main(){

    int N = 0 , i =0 , j=0;
    cin >> N >> i >> j;

    cout << min(abs(j-i)-1, min(i, j) + N - max(i, j)-1);


    return 0;
}