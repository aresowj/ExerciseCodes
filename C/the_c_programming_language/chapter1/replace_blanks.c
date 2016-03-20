/* a program copies its input to its output, 
 * replacing each string of one or more blanks 
 * by a single blank.
 */

#include <stdio.h>

main()
{
    int last_char = 0;
    int c;

    while (c != EOF) {
        c = getchar();
        if (!(c == ' ' && last_char == ' ')) {
            putchar(c);
        }
        last_char = c;
    }
}

