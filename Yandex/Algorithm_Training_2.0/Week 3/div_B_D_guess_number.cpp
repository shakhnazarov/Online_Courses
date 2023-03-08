#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#define ENDLINE '\n'
using namespace std;

int main(){
    int n=0;
    cin >> n;
    string inp;
    set<int> nums_ans, nums_temp, nums_wrong, nums_right, nums_temp_right;

    while (cin>>inp){
        if(inp == "YES"){
            if(nums_right.empty()) {
                for (const auto &item1: nums_temp) {
                    nums_right.insert(item1);
                }
            } else{
                for (const auto& item : nums_right){
                    if(nums_temp.count(item)==1){
                        nums_temp_right.insert(item);//nums_right.erase(item); мб нельзя удалять элемент
                    }
                }
                nums_right=nums_temp_right;
                nums_temp_right.clear();
            }

            nums_temp.clear();
        } else if(inp == "NO"){
            for (const auto& item : nums_temp){
                nums_wrong.insert(item);
            }
            nums_temp.clear();
        } else if(inp == "HELP"){
            break;
        } else {
            nums_temp.insert(stoi(inp));
        }
    }

    if(nums_right.empty()) {
        for (int i = 1; i < n + 1; ++i) {
            nums_right.insert(i);
        }
    }

    for (const auto& item : nums_wrong){
        nums_right.erase(item);
    }
// вдруг мы удалим весь nums_right

    for(const auto& item : nums_right) {
        cout << item << " ";
    }


    return 0;
}