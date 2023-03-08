#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

void CHANGE_CAPITAL (map<string, string>& mappy){
    string country, capital;
    cin >> country >> capital;
    if(mappy.count(country) == 0){
        cout << "Introduce new country " << country <<" with capital " << capital;
    } else if(mappy[country] == capital){
        cout << "Country " << country << " hasn't changed its capital";
    } else {
        cout << "Country " << country <<  " has changed its capital from " << mappy[country] << " to " << capital;
    }
    cout << ENDLINE;
    mappy[country] = capital;

}

void RENAME (map<string, string>& mappy){
    string country_old, country_new;
    cin >> country_old >> country_new;
    if ((country_old == country_new) || (mappy.count(country_old) == 0) || (mappy.count(country_new) == 1)){
        cout << "Incorrect rename, skip";
    } else {
        cout << "Country " << country_old << " with capital " << mappy[country_old] << " has been renamed to " << country_new;
        mappy[country_new] = mappy[country_old];
        mappy.erase(country_old);
    }
    cout << ENDLINE;
}

void ABOUT (map<string, string>& mappy){
    string country;
    cin >> country;
    if (mappy.count(country) == 0) {
        cout << "Country " << country << " doesn't exist";
    } else {
        cout << "Country " << country <<  " has capital " << mappy[country];
    }
    cout << ENDLINE;
}

void DUMP(const map<string, string>& mappy) {
    if (mappy.empty()) {
        cout << "There are no countries in the world";
    } else {
        for (const auto &elem: mappy) {
            cout << elem.first << "/" << elem.second << " ";
        }

    }
    cout << ENDLINE;
}

int main() {
    int Q;
    cin >> Q;
    string com;
    map<string, string> book;
    //enum commands {ADD = 1, DUMP = 2, NEXT = 3};
    for (int i = 0; i < Q; ++i) {
        cin >> com;
        if (com == "CHANGE_CAPITAL") {
            CHANGE_CAPITAL(book);
        }
        if (com == "RENAME") {
            RENAME(book);
        }
        if (com == "ABOUT") {
            ABOUT(book);
        }
        if (com == "DUMP") {
            DUMP(book);
        }
    }
    return 0;
}