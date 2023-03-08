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

    int N, M;
    cin >> N >> M;
    vector<int> groups(N), rooms(M);
    for (int i = 0; i < N; ++i) {
        cin >> groups[i];
    }
    for (int i = 0; i < M; ++i) {
        cin >> rooms[i];
        rooms[i]--;
    }

    vector<int> groups_copy = groups, rooms_copy = rooms;
    //reverse сортировка
    std::sort(groups_copy.begin(), groups_copy.end(), greater<>());
    std::sort(rooms_copy.begin(), rooms_copy.end(), greater<>());

    int P=0, last=0;
    vector<int> ans(N, 0);
    for (int first = 0; first < N; ++first) {
        while(last < rooms.size() && rooms_copy[last] >= groups_copy[first]){
            auto it_group = find(groups.begin(), groups.end(), groups_copy[first]);
            auto it_room = find(rooms.begin(), rooms.end(), rooms_copy[last]);
            *it_group = -1;
            *it_room = -1;
            ans[it_group - groups.begin()] = it_room - rooms.begin() + 1;
            ++P;
            ++last;
            break;
        }
    }

    cout << P << ENDLINE;
    for (int i = 0; i < N; ++i) {
        cout << ans[i] << ENDLINE;
    }
    
    return 0;
}