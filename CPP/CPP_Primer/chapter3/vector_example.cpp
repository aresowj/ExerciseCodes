#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::vector<std::string> s;
    std::string s1 = "String 1";
    s.push_back(s1);
    s.push_back(std::string("abc"));
    for (std::string str : s)
        std::cout << str << std::endl;
    
    std::cout << s.empty() << std::endl;
    return 0;
}

