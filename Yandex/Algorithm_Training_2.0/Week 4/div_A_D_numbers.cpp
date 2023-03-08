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

    string A, B;
    cin >> A >> B;
    map<char, vector<int>> numbers;

    int A_len=A.length(), B_len=B.length();
    bool is_A_max = (A_len==max(A_len,B_len));
    for (int i=0; i<min(A.length(), B.length()); ++i){
        if(numbers.count(A[i])==0){
            numbers[A[i]].push_back(0);
            numbers[A[i]].push_back(0);
        }
        numbers[A[i]][0]++;

        if(numbers.count(B[i])==0){
            numbers[B[i]].push_back(0);
            numbers[B[i]].push_back(0);
        }
        numbers[B[i]][1]++;
    }

    if(is_A_max) {
        for (int i = min(A.length(), B.length()); i < max(A.length(), B.length()); ++i) {
            if (numbers.count(A[i]) == 0) {
                numbers[A[i]].push_back(0);
                numbers[A[i]].push_back(0);
            }
            numbers[A[i]][0]++;
        }
    } else {
        for (int i = min(A.length(), B.length()); i < max(A.length(), B.length()); ++i) {
            if (numbers.count(B[i]) == 0) {
                numbers[B[i]].push_back(0);
                numbers[B[i]].push_back(0);
            }
            numbers[B[i]][1]++;
        }
    }

    bool is_empty_output = true, has_no_leading_zeros  = false;
    for(auto it = numbers.rbegin(); it!=numbers.rend(); ++it){
        if(numbers[it -> first][0] > numbers[it -> first][1]){
            numbers[it -> first].erase(numbers[it -> first].begin());
        } else{
            numbers[it -> first].pop_back();
        }
        if(it -> first !='0'){

            for (int i = 0; i < it -> second[0]; ++i) {
                has_no_leading_zeros = true;
                cout << it -> first;
            }
        } else if(has_no_leading_zeros){
            for (int i = 0; i < it -> second[0]; ++i) {
                cout << it -> first;
            }
        } else if(it -> second[0] > 0){
            cout << "0";
        }
        if (it -> second[0] > 0){
            is_empty_output = false;
        }
    }

    if(is_empty_output){
        cout << -1;
    }

    return 0;
}