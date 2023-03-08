#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//как ещё можно объявлять переменные?
const vector<int> DAYS = {
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
};

void ADD (vector<vector<string>>& vec){
    int i;
    cin >> i;
    --i;
    string bus;
    cin >> bus;
    vec[i].push_back(bus);

}

void DUMP(const vector<vector<string>>& vec){
    int i;
    cin >> i;
    --i;
    cout << vec[i].size() << " ";
    for (const auto& elem : vec[i]){
        cout << elem << " ";
    }
    cout << "\n";
}

void NEXT(vector<vector<string>>& vec, int& k) {
    ++k;
  //  if ( k == 12) {
   //     k = 0;
  //  }
    k = k%DAYS.size();
    if (k != 0){
        if( DAYS[k] - DAYS[k-1] > 0) {
            vec.resize(DAYS[k]);
        } else {
            for (int i = DAYS[k]; i < DAYS[k-1]; ++i){
                vec[DAYS[k]-1].insert(vec[DAYS[k]-1].end(), vec[i].begin(), vec[i].end());
            }
            vec.resize(DAYS[k]);
        }
    }
}


int main() {
    int Q, K = 0;
    cin >> Q;
    string com;
    vector<vector<string>> list(31);
    //enum commands {ADD = 1, DUMP = 2, NEXT = 3};
    for (int i = 0; i < Q; ++i) {
        cin >> com;
        if (com == "ADD") {
            ADD(list);
        }
        if (com == "DUMP") {
            DUMP(list);
        }
        if (com == "NEXT") {
            NEXT(list, K);
        }
    }
        return 0;
}