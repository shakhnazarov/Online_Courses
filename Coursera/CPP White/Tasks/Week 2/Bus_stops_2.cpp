#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;


int main() {
    int Q, N, size=0;
    cin >> Q;
    string stop;
    map< vector<string>, int> routes;
    vector<string> stops;
    //enum commands {ADD = 1, DUMP = 2, NEXT = 3};
    for (int i = 0; i < Q; ++i) {
        stops.clear();
        cin >> N;
        for (int j = 0; j < N; ++j) {
            cin >> stop;
            stops.push_back(stop);
        }
        if (routes.count(stops) == 0){
            size = routes.size() + 1;
            routes[stops] = size;
            cout << "New bus " << size << ENDLINE;
        } else {
            cout << "Already exists for " << routes[stops] << ENDLINE;
        }
    }
    return 0;
}