#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <unordered_set>
#include <map>
#define ENDLINE "\n"

using namespace std;

int main(){
    int n;
    cin >> n;
    long long int d, a;
    map<long long int, vector<long long int>> delivery;
    for (int i = 0; i < n; ++i) {
        cin >> d >> a;
        delivery[d].push_back(a);
    }

    for (const auto& item : delivery){
        long long int sum = 0;
        for(const auto& num : item.second){
            sum+=num;
        }
        cout << item.first << " " << sum << ENDLINE;
    }

    return 0;
}