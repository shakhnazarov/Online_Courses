#include <iostream> //Библиотека ввода и вывода
#include <string> //Чтобы уметь юзать Стринг
#include <vector>
#include <map> // dictionary

using namespace std;

struct Person { //create свой собственный тип
    string name;
    string surname;
    int age;
};

int main() {
    cout << "Hello, World\n";

    //ПОиграемся с типами
    int x = -5;
    char Z = 'Z';
    map<string, int> name_to_value; //value of umexisted key is 0
    string s = "ya volna";
    vector<int> a = {1, 2, 3, 5};

    cout << a.size() << " \n" << name_to_value["ome"];
    // Присваивание создаёт полную глубокую копию (в том числе для вектора) (не как в Питон)
    int sis = 1;
    int tis = sis;
    tis = 2;

    //map
    map<string, int> mappy = {{"a", 1}, {"b", 2}};
    string  concat;
    int sum = 0;
    for (const auto& elem : mappy) {
        concat += elem.first;
        sum += elem.second;
        if (sum == 1){
            break;
        }
    }
    cout << concat << " " << sum;
    //Struct

    vector<Person> classmates;

    classmates.push_back({"Averin", "Averinio", 31});
    cout << classmates[0].surname; //cout не выводит элемент из classmates
    return 0;
}
