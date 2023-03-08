#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s = "abvdf";
    for (auto c : s) { //перебираем все элементы в контейнере(?)
        cout << c << ", ";
    }

    //заюзаем билиотеку алгоритм для подсчёта элементов
    int quantity = count(s.begin(), s.end(), 'a');
    cout << quantity;

    // как выододятся массивы и сортируются
    vector<int> vec = {1, 3, 2};

    sort(vec.begin(), vec.end());
    for (auto i : vec) {
        cout << i << " ";
    }
    return 0;
}