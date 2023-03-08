#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    int num, xs = 0, circles = 0, zeros = 0;
    vector<vector<int>> matrix(3);
    for (int i = 0; i <3; ++i){
        for(int j =0; j<3; ++j){
            cin >> num;
            if(num == 2){
                zeros++;
            } else if(num==1){
                xs++;
            } else {
                circles++;
            }

            matrix[i].push_back(num);
        }
    }
    if (xs - zeros > 1 || xs - zeros < 0){
        cout << "NO";
        return 0;
    }
    if (xs>5 || zeros > 4){
        cout << "NO";
        return 0;
    }

    int count_3s = 0;

    for (const auto& item : matrix){
        if(count(item.begin(), item.end(), 1) == 3 || count(item.begin(), item.end(), 2) == 3){
            count_3s++;
        }
    }

    for (int i =0; i<3; ++i){
        set<int> set1;
        set1.insert(matrix[0][i]);
        set1.insert(matrix[1][i]);
        set1.insert(matrix[2][i]);
        if(set1.size()==1 && set1.count(0) != 1){
            count_3s++;
        }
    }

    set<int> s2 = {matrix[0][0], matrix[1][1], matrix[2][2]}, s3 = {matrix[2][0], matrix[1][1], matrix[0][2]};

    if((s2.size()==1 && s2.count(0)!=1)){
        count_3s++;
    }
    if(s3.size()==1 && s3.count(0) !=1){
        count_3s++;
    }
    if(count_3s > 1 || count_3s == 1 && xs==zeros){
        cout << "NO";
    } else{
        cout << "YES";
    }

    return 0;
}