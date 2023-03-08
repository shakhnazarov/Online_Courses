#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void MoveStrings (vector<string>& source, vector<string>& destination) {
    for (auto word : source) {
        destination.push_back(word);
    }
    source.clear();
}

int main() {
    vector<string> a = {"a", "b", "c"}, b ={"a", "b"};
    MoveStrings(a,b);
    return 0;
}