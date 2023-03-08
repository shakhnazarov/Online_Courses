#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    //деление целых числе по floor
    int a = 12, b = 5;
    a /= 2;
    cout << a/b;

    // logical
    vector<int> vec1 = {1, 2, 3}, vec2 = {1, 3, 2}; // order of elements is important
    if (vec1 == vec2 || true) {
      cout << "yes it ius";
    }


    return 0;
}