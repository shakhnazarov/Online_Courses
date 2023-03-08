#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

void NEW_BUS (map<string, vector<string>>& mappy, vector<string>& buses){
    string bus, stop;
    int N;
    cin >> bus >> N;
    for (int i = 0; i<N; ++i) {
        cin >> stop;
        mappy[bus].push_back(stop);
    }
    buses.push_back(bus);
}

void BUSES_FOR_STOP (map<string, vector<string>>& mappy, const vector<string>& buses){
    string stop;
    int k =0;
    cin >> stop;
    for (const auto& bus : buses) {
        if (find(mappy[bus].begin(), mappy[bus].end(), stop) != mappy[bus].end()){
            cout << bus << " ";
            ++k;
        }
    }
    (k !=0) ? cout << ENDLINE : cout << "No stop" << ENDLINE;
}


void STOPS_FOR_BUS (map<string, vector<string>>& mappy, vector<string>& buses){
    string bus;
    int k = 0;
    cin >> bus;
    if (find(buses.begin(), buses.end(), bus) != buses.end()){
        for (auto stop : mappy[bus]) {
            cout << "Stop " << stop << ": ";
            for (const auto& bus_iter : buses) {
                if (bus != bus_iter && find(mappy[bus_iter].begin(), mappy[bus_iter].end(), stop) != mappy[bus_iter].end()){
                    cout << bus_iter << " ";
                    ++k;
                }
            }
            (k !=0) ? cout << ENDLINE : cout << "no interchange" << ENDLINE;
            k = 0;
        }

    } else {
        cout << "No bus" << ENDLINE;
    }
}

void ALL_BUSES(map<string, vector<string>>& mappy) {
    if (!mappy.empty()) {
        for (auto item : mappy){
            cout << "Bus " << item.first << ": ";
            for (auto stop : item.second) {
                cout << stop << " ";
            }
            cout << ENDLINE;
        }
    } else {
        cout << "No buses" << ENDLINE;
    }
}

int main() {
    int Q;
    cin >> Q;
    string com;
    map<string, vector<string>> all_stops;
    vector<string> buses;
    //enum commands {ADD = 1, DUMP = 2, NEXT = 3};
    for (int i = 0; i < Q; ++i) {
        cin >> com;
        if (com == "NEW_BUS") {
            NEW_BUS(all_stops, buses);
        }
        if (com == "BUSES_FOR_STOP") {
            BUSES_FOR_STOP(all_stops, buses);
        }
        if (com == "STOPS_FOR_BUS") {
            STOPS_FOR_BUS(all_stops, buses);
        }
        if (com == "ALL_BUSES") {
            ALL_BUSES(all_stops);
        }
    }
    return 0;
}