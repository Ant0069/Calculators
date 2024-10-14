#include <iostream>
using namespace std;

int main() {
    cout << "Enter a Temp: ";
    double Fahrenheit;
    cin>> Fahrenheit;
    double Celsius = (Fahrenheit -32)* 5 /9;
    cout << Celsius;
    return 0;
}