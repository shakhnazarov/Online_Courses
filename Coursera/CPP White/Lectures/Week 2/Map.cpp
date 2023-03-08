#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#define ENDLINE "\n"
//можем замерять работу программы
#include <chrono>
using namespace std;

void PrintMap(const map<int,string>& dict) {
    for (auto item : dict) {
        cout << item.first << ": " << item.second << ENDLINE ;
    }
}

int main() {
    //ключи в мапе хранятся отсортированно
    // dictionary is associative set
    map<int, string> event;
    event[123] = "123123";

    //можем удалить ключ
    event.erase(123);

    //в c++ 17
    for(auto& [key, value] : event){
        cout << key << value;
    }
    //игнорится 3-е значением
    map<int, string> m = {{1, "odd"}, {2, "even"}, {1, "one"}};
    PrintMap(m);
    m.erase(1231);
    return 0;
}