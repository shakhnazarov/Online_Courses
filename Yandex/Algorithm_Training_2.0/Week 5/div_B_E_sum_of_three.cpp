#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <unordered_set>
#include <vector>
#define ENDLINE "\n"

using namespace std;

int main(){

    int S, n1, n2, n3;
    cin >> S >> n1;

    vector<int> nums1(n1);
    for (int i = 0; i < n1; ++i) {
        cin >> nums1[i];
    }

    cin >> n2;
    vector<int> nums2(n2);
    for (int i = 0; i < n2; ++i) {
        cin >> nums2[i];
    }

    cin >> n3;
    vector<int> nums3(n3);
    for (int i = 0; i < n3; ++i) {
        cin >> nums3[i];
    }

    int now_sum = 0, first= 0, second = 0, third=0;
    for (third = 0; third < n3; ++third) {
        while (second < n2){
            while (first < n1 && first > -1){
                now_sum = nums1[first] + nums2[second] + nums3[third];
                if(now_sum > S){
                    break;
                }
            }
        }
    }
}