#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>
#include <set>
#include <vector>
#include <unordered_set>
#define ENDLINE "\n"

using namespace std;

int main(){

    string line, word;
    vector<string> party_name;
    vector<string> party_names_ans;
    int votes, sum=0;
    map<string, vector<double>> party_votes;
    while(getline(cin, line)){
        if (line == "q"){
            break;
        }
        party_name.clear();
        stringstream s(line);
        while (getline(s, word, ' ')){
            party_name.push_back(word);
        }
        votes = stoi(party_name.back());
        sum+= votes;
        party_name.pop_back();
        string party_name_string = party_name.front();
        for(const auto& part : party_name){
            if(part!=party_name_string){
                party_name_string+=" " + part;
            }
        }
        party_names_ans.push_back(party_name_string);
        party_votes[party_name_string].push_back(votes);
    }


    double first_vote_number = sum/450.0;
    int sum_mandates=0;
    for (const auto& item : party_votes){
        party_votes[item.first].push_back(int(item.second[0]/first_vote_number));
        party_votes[item.first].push_back(item.second[0]/first_vote_number-int(item.second[0]/first_vote_number));
        sum_mandates+=int(item.second[0]/first_vote_number);

    }

    while(sum_mandates != 450){
        double max = -1;
        unordered_set<string> party_names_rivals_for_additional_vote;
        for (const auto& item : party_votes){
            if(max==item.second[2]){
                party_names_rivals_for_additional_vote.insert(item.first);
            } else if(max < item.second[2]){
                party_names_rivals_for_additional_vote.clear();
                max = item.second[2];
                party_names_rivals_for_additional_vote.insert(item.first);
            }
        }

        if(party_names_rivals_for_additional_vote.size() <= 450-sum_mandates){
            for (const auto& item : party_names_rivals_for_additional_vote){
                party_votes[item][1]++;
                party_votes[item][2]=0;
                sum_mandates++;
            }
        } else{
            while(sum_mandates != 450){
                string party_max;
                int max_initial_votes = -1;
                for (const auto& item : party_votes){
                    if(max_initial_votes<item.second[0]){
                        max_initial_votes = item.second[0];
                        party_max = item.first;
                    }
                }
                party_votes[party_max][1]++;
                party_votes[party_max][2]=0;
                sum_mandates++;
            }
        }
    }

    for(const auto& item : party_names_ans){
        int final_votes = 0;
        for(const auto& item1 : party_votes){
            if (item1.first==item){
                final_votes=item1.second[1];
                break;
            }
        }
        cout << item << " " << final_votes << ENDLINE;
    }

    return 0;
}