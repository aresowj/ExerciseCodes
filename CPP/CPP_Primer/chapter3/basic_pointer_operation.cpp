#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *e = &arr[10];
    for (int *b = arr; b != e; ++b)
        cout << "Value at " << b << " is " << *b << endl;
    return 0;
}
