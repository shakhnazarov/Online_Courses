#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;

int main(){
    int num=0;
    int max=0;
    int count = 0;
    while(cin>>num){
        if(num==0){
            break;
        }
        if(num > max){
            max=num;
            count = 1;
        } else if(num==max){
            count++;
        }

    }

    cout << count;


    //пустая последов или один симовл
    return 0;
}