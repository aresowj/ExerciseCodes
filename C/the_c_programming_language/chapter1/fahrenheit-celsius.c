#include <stdio.h>

/* print Fahrenheit-Celsius table
 * for fahr = 0, 20, ..., 300 */

#define LOWER 0     /* lower limit of table */
#define UPPER 300   /* upper limit */
#define STEP  20    /* step size */

main()
{
    int fahr;

    for ( fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
    /* float fahr, celsius; */
    /* int lower, upper, step; */

    /*
    lower = 0;  // lower limit of temperature table
    upper = 300;    // upper limit
    step = 20;  // step size

    fahr = lower;

    while(fahr <= upper) {
        celsius = 5.0 * (fahr-32.0) / 9.0;
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
    */


}

