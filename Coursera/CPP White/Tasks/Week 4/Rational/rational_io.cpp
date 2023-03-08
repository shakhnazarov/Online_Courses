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
int main() {
    {
        ostringstream output;
        output << Rational(-6, 8);
        if (output.str() != "-3/4") {
            cout << "Rational(-6, 8) should be written as \"-3/4\"" << endl;
            return 1;
        }
    }

    {
        istringstream input("5/7");
        Rational r;
        input >> r;
        bool equal = r == Rational(5, 7);
        if (!equal) {
            cout << "5/7 is incorrectly read as " << r << endl;
            return 2;
        }
    }

    {
        istringstream input("");
        Rational r;
        bool correct = !(input >> r);
        if (!correct) {
            cout << "Read from empty stream works incorrectly" << endl;
            return 3;
        }
    }

    {
        istringstream input("5/7 10/8");
        Rational r1, r2;
        input >> r1 >> r2;
        bool correct = r1 == Rational(5, 7) && r2 == Rational(5, 4);
        if (!correct) {
            cout << "Multiple values are read incorrectly: " << r1 << " " << r2 << endl;
            return 4;
        }

        input >> r1;
        input >> r2;
        correct = r1 == Rational(5, 7) && r2 == Rational(5, 4);
        if (!correct) {
            cout << "Read from empty stream shouldn't change arguments: " << r1 << " " << r2 << endl;
            return 5;
        }
    }

    {
        istringstream input1("1*2"), input2("1/"), input3("/4");
        Rational r1, r2, r3;
        input1 >> r1;
        input2 >> r2;
        input3 >> r3;
        bool correct = r1 == Rational() && r2 == Rational() && r3 == Rational();
        if (!correct) {
            cout << "Reading of incorrectly formatted rationals shouldn't change arguments: "
                 << r1 << " " << r2 << " " << r3 << endl;

            return 6;
        }
    }

    {
        istringstream input("2/4/6/8");
        Rational r1;
        input >> r1;
        bool correct = r1 == Rational(1, 2);
        if (!correct) {
            cout << "Multiple-slashed number sequence value read incorrectly: " << r1 << endl;
            return 7;
        }
    }

    cout << "OK" << endl;
    return 0;
}
