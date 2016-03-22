#include <iostream>
main()
{
    int v1 = 0, v2 = 0;
    /* print 'Hello, World' on the standard output. */
    std::cout << "Hello, World" << std::endl;
    
    /* write a program to print a multiplication result */
    std::cout << "Enter two numbers:" << std::endl;
    std::cin >> v1 >> v2;
    std::cout << "The result is: " << v1 * v2 << std::endl;

    return 0;
}

