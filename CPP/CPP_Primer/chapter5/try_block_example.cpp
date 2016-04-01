#include <iostream>
#include <stdexcept>
using std::runtime_error;
using std::cout;
using std::cin;
int main()
{
    double a = 1, b = 1;

    try {
        cout << "Enter the dividend: ";
        cin >> a;
        cout << "Enter the divisor: ";
        cin >> b;
        if (b == 0)
            throw runtime_error("Divisor is zero!\n");
        cout << "Result is " << a / b << std::endl;
    } catch (runtime_error err) {
        cout << "Runtime Error caught:" << std::endl;
        cout << "\t" << err.what();
    }
    return 0;
}

