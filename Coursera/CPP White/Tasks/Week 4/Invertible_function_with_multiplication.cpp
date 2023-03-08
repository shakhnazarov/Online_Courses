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

/*.struct Image {
    double quality;
    double freshness;
    double rating;
};

struct Params {
    double a;
    double b;
    double c;
};
*/
class FunctionPart{
public:
    FunctionPart(const char& new_sign, const double& new_value){
        sign = new_sign;
        part = new_value;
    }

    double GetPart() const{
        return part;
    }
    char GetSign() const{
        return sign;
    }
    void SetSign(const char& new_sign){
        sign = new_sign;
    }
private:
    char sign;
    double part;
};

class Function{

public:
    void AddPart(const char& let, const double & functionPart){
        parts.push_back({let, functionPart});
    }

    double Apply(double value) const{
        for (const auto& part : parts){
            if (part.GetSign() == '+'){
                value += part.GetPart();
            } else if (part.GetSign() == '-') {
                value -= part.GetPart();
            } else if (part.GetSign() == '*'){
                value *= part.GetPart();
            } else {
                value /= part.GetPart();
            }
        }
        return value;
    }

    void Invert() {
        reverse(parts.begin(), parts.end());
        for (auto& part : parts){
            if (part.GetSign() == '+'){
                part.SetSign('-');
            } else if (part.GetSign() == '-') {
                part.SetSign('+');
            } else if (part.GetSign() == '*'){
                part.SetSign('/');
            } else {
                part.SetSign('*');
            }
        }
    }

    vector<FunctionPart> parts;
};

Function MakeWeightFunction(const Params& params,
                            const Image& image) {
    Function function;
    function.AddPart('*', params.a);
    function.AddPart('-', image.freshness * params.b);
    function.AddPart('+', image.rating * params.c);
    return function;
}

double ComputeImageWeight(const Params& params, const Image& image) {
    Function function = MakeWeightFunction(params, image);
    return function.Apply(image.quality);
}

double ComputeQualityByWeight(const Params& params,
                              const Image& image,
                              double weight) {
    Function function = MakeWeightFunction(params, image);
    function.Invert();
    return function.Apply(weight);
}



