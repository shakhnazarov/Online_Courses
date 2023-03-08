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
            throw invalid_argument("division by zero");
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
        throw domain_error("division by zero");
    }
    return Rational(
            lhs.Numerator()*rhs.Denominator(),
            lhs.Denominator() * rhs.Numerator()
    );
}



int main() {
    try {
        Rational r(1, 0);
        cout << "Doesn't throw in case of zero denominator" << endl;
        return 1;
    } catch (invalid_argument&) {
    }

    try {
        auto x = Rational(1, 2) / Rational(0, 1);
        cout << "Doesn't throw in case of division by zero" << endl;
        return 2;
    } catch (domain_error&) {
    }

    cout << "OK" << endl;
    return 0;
}
