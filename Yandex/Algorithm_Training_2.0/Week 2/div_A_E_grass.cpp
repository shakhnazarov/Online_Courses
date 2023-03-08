#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>

using namespace std;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    int x3, y3, r, ans=0;
    cin >> x3 >> y3 >> r;

    for(int i =max(x3-r, x1); i<=min(x3+r, x2);++i){
        for (int j = max(y3-r,y1); j <= min(y3+r, y2); ++j) {
            if(x1<=i && i<=x2 && y1<=j && j<=y2 && sqrt( pow((i-x3), 2) + pow((j-y3),2))<=r){
                ans++;
            }
        }
    }
    cout << ans;
    return 0;
}
    /*
    set<vector<int>> cut_points;
    int ans=0;
    for(int i =x1; i<=x2;++i){
        for (int j = y1; j <= y2; ++j) {
            if(sqrt( pow((i-x3), 2) + pow((j-y3),2))<=r){
                ans++;
            }
        }
    }

    cout << ans;
*/



