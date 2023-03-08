#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <unordered_set>
#include <map>
#define ENDLINE "\n"

using namespace std;

map<string, unordered_set<string>> Solution(const vector<string>& input_vector){
    map<string, unordered_set<string>> ans;
    for(const auto& word : input_vector){
        string word_sorted = word;
        sort(word_sorted.begin(), word_sorted.end());
        ans[word_sorted].insert(word);
    }
    return ans;
}

int main(){
    int n;
    cin >> n;
    long long int d, a;
    map<long long int, unordered_set<long long int>> delivery;
    for (int i = 0; i < n; ++i) {
        cin >> d >> a;
        delivery[d].insert(a);
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