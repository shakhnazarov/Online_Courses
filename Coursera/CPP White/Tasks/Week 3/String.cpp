#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

class ReversibleString{
public:
    ReversibleString(){
        string_ini = "";
    }
    ReversibleString(const string& str) {
        string_ini =str;
    }

public:
    string ToString() const{
        return string_ini;
    }

    void Reverse (){
        int N = string_ini.size();
        //reverse(string_ini.begin(), string_ini.end());
        string string_rev ="";
        for (int i = N-1; i>-1; --i){
            string_rev+=string_ini[i];
        }
        string_ini = string_rev;
    }

private:
    string string_ini;
};

int main() {
    ReversibleString s("live");
    s.Reverse();
    cout << s.ToString() << endl;

    s.Reverse();
    const ReversibleString& s_ref = s;
    string tmp = s_ref.ToString();
    cout << tmp << endl;

    ReversibleString empty;
    cout << '"' << empty.ToString() << '"' << endl;

    return 0;
}
