#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <string>
#include <sstream>
#include <unordered_set>
#include <map>
#define ENDLINE "\n"

using namespace std;

int main(){

    string A, B, ans;
    cin >> A >> B;
    map<char, vector<int>> numbers;


    char i='z';
    while(i >= 'a'){
        if(A.find(i) != string::npos && B.find(i) != string::npos){
            ans+=i;
            A = A.substr(A.find(i)+1);
            B = B.substr(B.find(i)+1);
        } else{
            --i;
        }
    }

    cout << ans;
    return 0;
}