#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <unordered_set>
#include <vector>
#define ENDLINE "\n"

using namespace std;

int main(){

    string line;
    cin >> line;
    int queue=0;
    for(const auto& item : line){
        if(item == '('){
            queue++;
        } else{
            queue--;
        }
        if(queue<0){
            cout << "NO";
            break;
        }
    }
    if(queue>0){
        cout << "NO";
    } else if(queue==0){
        cout << "YES";
    }

    return 0;
}