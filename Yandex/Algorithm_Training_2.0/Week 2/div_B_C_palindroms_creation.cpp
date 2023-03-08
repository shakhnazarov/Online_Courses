#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    string string1;
    cin >> string1;

    int count = 0;
    for (int i=0; i<string1.size()/2; ++i){
        if(string1[i]!=string1[string1.size()-i-1]){
            count++;
        }
    }

    cout << count;
    return 0;
}