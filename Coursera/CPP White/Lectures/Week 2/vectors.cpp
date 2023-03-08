#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

//можем замерять работу программы
#include <chrono>
using namespace std;
using namespace std::chrono;

void PringVector (const vector<string>& vec) {
    for (auto& v : vec) {
        cout << v << "\n";
    }
}

int main() {
    int N;
    cin >> N;

    vector<string> lectors(N, "jinga"); //Можем задавать размер массива
    //можем по одному значениею вписывать
    int i = 0;
    string word;
    while (i<N){
        cin >> word;
        lectors.push_back(word); // у нас уже размер ветокра 10 - будет 20
        cout << "current " << lectors.size() << "\n";
        ++i;
    }
    PringVector(lectors);

    lectors.resize(30) //мы не меняли изначальные занчения вектора
    lectors.assign(30, "jamalungma") //значения затёрли на новые
    return 0;
}