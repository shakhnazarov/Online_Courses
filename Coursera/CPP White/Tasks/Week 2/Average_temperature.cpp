#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

//можем замерять работу программы
#include <chrono>
using namespace std;
using namespace std::chrono;


void PrintVector (vector<int> vec) {
    for (int i; i<vec.size(); ++i){
        cout << vec[i] << " ";
    }
}

int main() {
    int N, sum = 0, K = 0;
    cin>> N;
    vector<int> temp(N), higher;
    // могли чрезе цикл прохождения по контейнеру ибо у нас уже есть размер вектора
    for (int i = 0; i<N; ++i) {
        cin >> temp[i];
        sum += temp[i];
    }

    int avg = sum/N;
    for (int i = 0; i<N; ++i){
        if (temp[i] > avg){
            higher.push_back(i);
            ++K;
        }
    }

    //вместо K можно было вывести просто размер вектора .size()
    cout << K << "\n";
    PrintVector(higher);

    return 0;
}