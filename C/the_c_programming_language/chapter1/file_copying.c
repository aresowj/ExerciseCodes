#include <stdio.h>

/* copy input to output; 2nd version */
main()
{
    int c;

    printf("Value of EOF:%d\n", EOF);

    while ((c = getchar()) != EOF) {
        putchar(c);
    }
}

