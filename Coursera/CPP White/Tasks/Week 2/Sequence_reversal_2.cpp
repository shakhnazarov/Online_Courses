#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<int> Reversed(const vector<int>& v){
    vector<int> vec_copy = v;
    int temp = 0, N = vec_copy.size();
    for (int i = 0; i < N / 2; ++i ) {
        temp = vec_copy[i];
        vec_copy[i] = vec_copy[N - i -1];
        vec_copy[N - i -1] = temp;
    }
    return vec_copy;
}

vector<int> ReversedSolution(const vector<int>& input)
{
    vector<int> result;
    for (int i = input.size() - 1; i >= 0; --i) {
        result.push_back(input[i]);
    }
    return result;
}

int main() {
    vector<int> numbers = {1, 5, 3, 4, 2};
    Reversed(numbers);
    return 0;
}