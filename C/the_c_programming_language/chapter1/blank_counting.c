/* a program counting blanks, tabs 
 * and new line in the input. 
 */

#include <stdio.h>

#define BLANK   ' '
#define TAB     '\t'
#define NEWLINE '\n'

main()
{
    int blanks, tabs, newlines, c;
    blanks = tabs = newlines = c = 0;

    while (c != EOF) {
        c = getchar();
        if (c == BLANK) {
            blanks++;
        } else if (c == TAB) {
            tabs++;
        } else if (c == NEWLINE) {
            c++;
        }
    }

    printf("\nBlanks: %d, Tabs: %d, Newlines: %d\n", blanks, tabs, newlines);
}

