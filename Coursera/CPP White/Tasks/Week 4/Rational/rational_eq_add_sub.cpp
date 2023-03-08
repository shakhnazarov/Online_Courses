#include <iostream>
#include <cmath>
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
        } else if(numerator < 0 && denominator > 0 || numerator > 0 && denominator < 0) {
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
            lhs.Numerator()*rhs.Denominator() + rhs.Numerator()*lhs.Denominator(),
            lhs.Denominator()*rhs.Denominator()
    );
}

Rational operator -(const Rational& lhs, const Rational& rhs){
    return Rational(
            lhs.Numerator()*rhs.Denominator() - rhs.Numerator()*lhs.Denominator(),
            lhs.Denominator()*rhs.Denominator()
    );
}

