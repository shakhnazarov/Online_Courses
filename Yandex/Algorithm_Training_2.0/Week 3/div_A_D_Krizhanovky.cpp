#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#include <fstream>
#include <map>
#include <sstream>
#define ENDLINE '\n'
using namespace std;

int main(){
    int N, temp;
    cin>> N;
    vector<int> initial_scores, guesses;
    vector<bool> is_duplicate(N, false);
    for (int i = 0; i < N; ++i) {
        cin >> temp;
        initial_scores.push_back(temp);
    }
    for(int i = 0 ; i< N-1; ++i){
        cin >> temp;
        auto it =find(guesses.begin(), guesses.end(), temp);
        if(it!=guesses.end()){
            is_duplicate.at(it-guesses.begin()) = true;
            is_duplicate.at(i) = true;
        }
        guesses.push_back(temp);
    }

    int max_people_beaten = -1;
    int ans_index;

        for (int j = 1; j < 102; ++j) {
            vector<int> initial_scores_copy=initial_scores;
            vector<bool> is_duplicate_copy = is_duplicate;
            vector<int> guesses_copy = guesses;
            auto it =find(guesses.begin(), guesses.end(), j);

            if(it!=guesses.end()){
                is_duplicate_copy.at(it-guesses.begin()) = true;
                is_duplicate_copy.back()=true;
            }

            int min_elem = 102, index;
            guesses_copy.push_back(j);
            for (int k = 0; k < N; ++k) {
                if(!is_duplicate_copy[k]){
                    if(min_elem > guesses_copy[k]){
                        min_elem = guesses_copy[k];
                        index = k;
                    }
                }
            }
            if(min_elem != 102){
                initial_scores_copy[index] += min_elem;
            }


            int people_beaten = 0;
            for (int k = 0; k < N; ++k) {
                if(initial_scores_copy.back()> initial_scores_copy[k]){
                    people_beaten++;
                }
            }
            if(max_people_beaten < people_beaten){
                max_people_beaten = people_beaten;
                ans_index = j;
            }
        }

        cout << ans_index;
    
    return 0;
}