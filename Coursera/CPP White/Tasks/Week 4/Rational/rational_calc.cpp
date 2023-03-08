#include <iostream>
#include <exception>
using namespace std;

class Rational {
public:
    Rational() {
        numerator = 0;
        denominator = 1;
    }

    Rational(int numerator, int denominator) {
        int gcd_ = gcd(numerator, denominator);
        if (denominator == 0){
            throw invalid_argument("Invalid argument");
        }
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
    if (rhs.Numerator() == 0){
        throw domain_error("Division by zero");
    }
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
    Rational r1, r2;
    char action;
    try{

        cin >> r1 >> action >> r2;
        if(action == '+'){
            cout << r1 + r2;
        } else if(action == '-'){
            cout << r1 - r2;
        } else if (action == '*'){
            cout << r1 * r2;
        } else {
            cout << r1 / r2;
        }
    } catch (exception& exc){
        cout << exc.what();
    }
}
