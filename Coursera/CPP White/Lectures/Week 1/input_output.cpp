#include <vector>
#include <iostream>
#include <string>
using namespace std;

int main() {
    vector<string> name = {"av", "asd"};
    for (auto v : name) {

    }

    string x  = "avc";
    string y = "vvv";
    cin >> x >> y; //парезаписываем значение переменной, можем ввести сразу 2 черзе пробл
    cout << x + y << "\n";

    //cycle
    int sum = 0, n =5;
    for (int i = 1; i <= n; ++i) {
        sum += i;
    }
    cout << sum;

    // не забывать что есть такое
    int a;
    do {
        cout << "vvedi number";
        cin >> a;
    } while (a!=0);


    return 0;
}