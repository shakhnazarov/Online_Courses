#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <string>
#include <sstream>
#include <unordered_set>
#include <map>
#define ENDLINE "\n"

using namespace std;


//Требуется из данных букв по указанным правилам составить палиндром наибольшей длины,
//а если таких палиндромов несколько, то выбрать первый из них в алфавитном порядке.
//есть баг, что тот элемент который мы вставляем посередине, может быть неминимальным
int main(){
    int n;
    cin >> n;
    string input_string;
    cin >> input_string;
    map<char, int> palindrome;

// Считаем сколько раз в слове считается каждый символ
    for (const char& letter : input_string) {
        if(palindrome.count(letter)==0){
            palindrome[letter]=0;
        }
        palindrome[letter]++;
    }

    set<char> odd_letters;
    int max = -1;

//хотим найти все нечётные элементы и уменьшить их количество на один
//кроме того, который встречается чаще всего (их может быть несколько)
    for(auto& item : palindrome){
        if(item.second%2==1) {
            if (max == item.second) {
                odd_letters.insert(item.first);
            } else if (max < item.second) {
                max = item.second;
                for (const auto &item1: odd_letters) {
                    palindrome[item1]--;
                }
                odd_letters.clear();
                odd_letters.insert(item.first);
            } else {
                item.second--;
            }
        }
    }

// в odd_letters сейчас все нечётные элементы с наибольшим count в изначальной строке
    char max_odd_letter;

// выбираем первый (самый маленький) элемент из массива, так как он отсортирован лексикографически
    if(!odd_letters.empty()){
        max_odd_letter = *odd_letters.begin();
    }

//уменьшаем оставшиеся нечётные элементы
    for(const auto& item1 : odd_letters){
        palindrome[item1]--;
    }

//Печатаем лексикографически самую маленькую часть (
    for(const auto& item : palindrome){
        for (int i = 0; i < item.second/2; ++i) {
            cout << item.first;
        }
    }

//если есть нечётные символы, то печатаем посередине один такой элемент
    if(!odd_letters.empty()) {
        cout << max_odd_letter;
    }

//допечатываем оставшуюся часть с конца (hence итератор)
    for(auto it=palindrome.rbegin(); it!=palindrome.rend(); it++){
        for (int i = 0; i < it -> second/2; ++i) {
            cout << it -> first;
        }
    }

    return 0;
}