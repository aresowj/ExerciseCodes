#include <iostream>
#include <stdexcept>

int main()
{
    double a = 1, b = 1;
    while (1) {
        std::cout << "Enter the first dividend: ";
        if (!(std::cin >> a))
            break;
        std::cout << "Enter the divisor: ";
        if (!(std::cin >> b))
            break;
        if ( b == 0 )
            throw std::runtime_error("Divisor must not be zero!");
        std::cout << a / b << std::endl;
    }
    return 0;
}

