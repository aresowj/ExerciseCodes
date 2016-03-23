#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<std::string> words;
    std::string w;
    while (std::getline(std::cin, w)) 
        words.push_back(w);
    for ( auto word:words )
        std::cout << "\"" <<  word << "\" ";
    std::cout << std::endl;

    return 0;
}

