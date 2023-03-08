#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void Reverse(vector<int>& v){
 int temp = 0, N = v.size();
 for (int i = 0; i < N / 2; ++i ) {
     temp = v[i];
     v[i] = v[N - i -1];
     v[N - i -1] = temp;
 }
}

int main() {
    vector<int> numbers = {1, 5, 3, 4, 2};
    Reverse(numbers);
    return 0;
}