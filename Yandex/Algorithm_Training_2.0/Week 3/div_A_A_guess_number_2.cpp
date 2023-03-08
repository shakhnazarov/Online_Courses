#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <set>
#include <fstream>
#include <sstream>
#define ENDLINE '\n'
using namespace std;

int main(){
    const string input_string = "input.txt";

    fstream input_file;
    input_file.open(input_string, ios::in);

    int n=0;
    input_file >> n;

    string inp, num_temp;
    while (getline(input_file, inp)){
        stringstream s(inp);
        unordered_set<int> nums_temp;
        while(getline(s, num_temp, ' ')){
            nums_temp.insert(stoi(num_temp));
        }


    }

               string inp;



    return 0;
}