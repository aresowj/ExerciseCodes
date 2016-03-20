/* a program copying its input to its output
 * and replace each tabs with '\t', backspace 
 * by '\b' and each backslash by '\\'. This 
 * makes tabs and backspaces visible in an 
 * unambiguous way.
 */

#include <stdio.h>

main()
{
    int c;

    while (c != EOF) {
        c = getchar();
        if (c == '\t') {
            putchar('\\');
            putchar('t');
        } else if (c == '\b') {
            putchar('\\');
            putchar('b');
        } else if (c == '\\') {
            putchar('\\');
            putchar('\\');
        } else {
            putchar(c);
        }
    }
}

