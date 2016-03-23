#include <iostream>
#include <vector>

int main()
{
    // count the number of grades by clusters of ten: 0--9, 10--19, ..., 90--99, 100
    std::vector<unsigned> scores(11, 0);
    unsigned grade;
    while (std::cin >> grade) {
        if (grade <= 100)
            ++scores[grade/10];
    }

    for (decltype(scores.size()) index = 0; index < scores.size(); index++)
        std::cout << scores[index] << " ";
    std::cout << std::endl;

    return 0;
}

