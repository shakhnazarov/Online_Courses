#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <cctype>
#include <fstream> //для работы с потоками
#include <iomanip> //для работы с  fixed выводом
#include <numeric>
#include <chrono> //можем замерять работу программы
#define ENDLINE "\n"


using namespace std;

class Rational {
public:
    Rational() {
        numerator = 0;
        denominator = 1;
    }

    Rational(int numerator, int denominator) {
        int gcd_ = gcd(numerator, denominator);
        if (numerator == 0) {
            this -> numerator = 0;
            this -> denominator = 1;
        } else if(numerator*denominator < 0) {
            this -> numerator = -1 * abs(numerator/gcd_);
            this -> denominator = abs(denominator/gcd_);
        } else {
            this -> numerator = abs(numerator/gcd_);
            this -> denominator = abs(denominator/gcd_);

        }
    }

    int Numerator() const {
        return numerator;
    }

    int Denominator() const {
        return denominator;
    }
private:

    int gcd(int a, int b){
        return a ? gcd(b%a, a) : b;
    }

    int numerator, denominator;
};


// Реализуйте для класса Rational операторы ==, + и -
bool operator ==(const Rational& lhs, const Rational& rhs){
    return lhs.Denominator() == rhs.Denominator() && lhs.Numerator() == rhs.Numerator();
}

Rational operator +(const Rational& lhs, const Rational& rhs){
    return Rational(
            rhs.Numerator()*lhs.Denominator() + lhs.Numerator()*rhs.Denominator(),
            lhs.Denominator()*rhs.Denominator()
    );
}

Rational operator -(const Rational& lhs, const Rational& rhs){
    return Rational(
            lhs.Numerator()*rhs.Denominator() - rhs.Numerator()*lhs.Denominator(),
            lhs.Denominator()*rhs.Denominator()
    );
}

Rational operator* (const Rational& lhs, const Rational& rhs){
    return Rational(
            rhs.Numerator() * lhs.Numerator(),
            lhs.Denominator() * rhs.Denominator()
    );
}

Rational operator/ (const Rational& lhs, const Rational& rhs){
    return Rational(
            lhs.Numerator()*rhs.Denominator(),
            lhs.Denominator() * rhs.Numerator()
    );
}

ostream& operator<< (ostream& ostream1, const Rational& rational){
    ostream1 << rational.Numerator() << "/" << rational.Denominator();
    return ostream1;
}

istream& operator>>(istream& ist, Rational& rational){
    //если бы просто оставить if(ist) то на закончимшимся istream будет true и только во второй раз false(?)
    char let;
    int num,den;
    if(ist >> num){
        ist >> let;
        if(let == '/' && ist >> den){
            rational = {num, den};
        }
    }
    return ist;
}

bool operator<(const Rational& lhs, const Rational& rhs){
    return double(lhs.Numerator())/lhs.Denominator() < double(rhs.Numerator())/rhs.Denominator();
}

// Реализуйте для класса Rational оператор(ы), необходимые для использования его
// в качестве ключа map'а и элемента set'а

int main() {
    {
        const set<Rational> rs = {{1, 2}, {1, 25}, {3, 4}, {3, 4}, {1, 2}};
        if (rs.size() != 3) {
            cout << "Wrong amount of items in the set" << endl;
            return 1;
        }

        vector<Rational> v;
        for (auto x : rs) {
            v.push_back(x);
        }
        if (v != vector<Rational>{{1, 25}, {1, 2}, {3, 4}}) {
            cout << "Rationals comparison works incorrectly" << endl;
            return 2;
        }
    }

    {
        map<Rational, int> count;
        ++count[{1, 2}];
        ++count[{1, 2}];

        ++count[{2, 3}];

        if (count.size() != 2) {
            cout << "Wrong amount of items in the map" << endl;
            return 3;
        }
    }

    cout << "OK" << endl;
    return 0;
}
