#include <stdio.h>

main()
{
    int c = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            printf("\n");
        } else if (c != '\n') {
            putchar(c);
        }
    }
}

