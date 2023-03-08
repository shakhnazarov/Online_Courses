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

    int N, num;
    string theme, message, num_str, N_str;
    getline(cin, N_str);
    N = stoi(N_str);

    map<string, unordered_set<int>> threads;
    vector<string> themes_chronological;

    for(int i=1; i<N+1; ++i){
        getline(cin, num_str);
        num = stoi(num_str);
        if(num==0){
            getline(cin, theme);
            threads[theme].insert(i);
            themes_chronological.push_back(theme);
        } else{
            for(const auto& item : threads){
                if(item.second.count(num)==1){
                    threads[item.first].insert(i);
                    break;
                }
            }
        }
        getline(cin, message);
    }

    map<string, vector<int>> ans;
    set<int> max_threads;
    int max = -1;
    for (const auto& item : threads){
        int index = 0;
        for(int i=0; i<themes_chronological.size(); ++i){
            if(themes_chronological[i]==item.first){
                index=i;
                break;
            }
        }
        int thread_size = item.second.size();

        if(max == thread_size){
            max_threads.insert(index);
        } else if(max < thread_size){
            max = thread_size;
            max_threads.clear();
            max_threads.insert(index);
        }



    }
    cout << themes_chronological[*max_threads.begin()];
    return 0;
}