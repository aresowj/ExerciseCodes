/* 
 * bare-bone version of the UNIX program wc.
 */

#include <stdio.h>

#define IN  1   /* inside a workd */
#define OUT 0   /* outside a word */

/* count lines, words, and characters in input */

main()
{
    int c, nl, nw, nc, state;

    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\n' || c == '\t')
            state == OUT;
        else if (state == OUT) {
            state = IN;
            ++nw;
        }
    }

    printf("%d line(s),  %d word(s),  %d char(s)\n", nl, nw, nc);
}

