#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){

    int N = 0, num;
    vector<int> pupils;
    cin >> N;
    for (int i = 0; i < N; ++i){
        cin >> num;
        pupils.push_back(num);
    }
    cout << pupils[N/2];

    return 0;
}