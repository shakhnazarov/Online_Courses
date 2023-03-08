#include <iostream>
using namespace std;

int main(){

    int r =0, c = 0, i=0;
    cin >> r >> i >> c;
    if(i==0){
        if(r!=0){
            cout << 3;
        } else {
            cout << c;
        }
    }
    if(i==1){
        cout << c;
    }
    if(i==4){
        if(r!=0){
            cout << 3;
        } else{
            cout << 4;
        }
    }
    if(i==6){
        cout << 0;
    }
    if(i ==7){
        cout << 1;
    }
    if( i== 2 || i ==3 || i == 5){
        cout << i;
    }

    return 0;
}