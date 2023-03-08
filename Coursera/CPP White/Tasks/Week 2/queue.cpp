#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int Q, num;
    cin >> Q;
    vector<string> coms(Q);
    vector<bool> ppl;
    for (auto com : coms) {
        cin >> com;
        if (com == "COME") {
            cin >> num;
            ppl.resize(ppl.size() + num, false);
        }
        if (com == "WORRY") {
            cin >> num;
            ppl[num] = true;
        }
        if (com == "WORRY_COUNT"){
            cout << count(ppl.begin(), ppl.end(), true);
        }
        if (com == "QUIET"){
            cin >> num;
            ppl[num] = false;
        }
    cout <<  endl;
    }

    return 0;
}