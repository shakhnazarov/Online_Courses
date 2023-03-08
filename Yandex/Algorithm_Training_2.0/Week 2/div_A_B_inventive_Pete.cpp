#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int main() {
    string machine, target;
    cin >> machine >> target;
    reverse(machine.begin(), machine.end());
    reverse(target.begin(), target.end());
    int k =0;
    int ans = target.length();
    for(int i=0; i<target.length(); ++i){
        if (target[i] == machine[k]){
            k = (k+1)%machine.length();
        } else{
            k=0;
            ans= target.length() - 1 - i;
        }
    }

    reverse(target.begin(), target.end());

    for (int i = ans; i < target.length(); ++i) {
        cout<<target[i];
    }

    return 0;
}




    /*
    //думаю можно как-то решить если уметь обновлять индекс у machine
    int i =0, k=0, count_prints=0;
    bool ended=false;
    while( i<target.length()){
        k=0;
        for(auto let : machine){
            if(target[i] == let){
                ++k;
            } else{
                break;
            }
            if(i==target.length()-1){
                ended = true;
                break;
            }
            ++i;
        }
        if(k==machine.length()-1){
            count_prints++;
        } else if(!ended){
            count_prints=0;
        }
        ++i;
    }
    reverse(target.begin(), target.end());
    for(int i=count_prints*machine.length()-1; i < target.length(); ++i){
        cout << target[i];
    }
    return 0;
}*/