#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#define ENDLINE '\n'
using namespace std;

int main(){
    int num, count=0;
    vector<int> nums;
    unordered_set<int> nums_duplicate;
    while (cin >> num){
        if(find(nums.begin(), nums.end(), num) != nums.end()){
            nums_duplicate.insert(num);
        }else{
            nums.push_back(num);
        }
    }

    for(const auto& item : nums_duplicate){
        auto position = std::find(nums.begin(), nums.end(), item);
        if(nums.end() != position){
            nums.erase(position);
        }  ;        //remove(nums.begin(), nums.end(), item);
    }


    for(const auto& item : nums){
        cout << item << " ";
    }

    return 0;
}