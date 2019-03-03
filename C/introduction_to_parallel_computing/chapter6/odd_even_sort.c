#include <stdlib.h>
#include <mpi.h>

int IncOrder(const void *e1, const void *e2)
{
    return (*((int *) e1) - *((int *) e2));
}

/* This is the CompareSplit function */
void CompareSplit(int nlocal, int *elements, int *relements, int *wspace, int keepsmall)
{
    int i, j, k;

    for (i = 0; i < nlocal; i++)
    {
        wspace[i] = elements[i];  // Copy the elements array into the wspace array
    }

    if (keepsmall)
    {
        // Keep the nlocal smaller elements
        for (i = j = k = 0; k < nlocal; k++)
        {
            if (j == nlocal || (i < nlocal && wspace[i] < relements[j]))
            {
                elements[k] = wspace[i++];
            }
            else
            {
                elements[k] = relements[j++];
            }
        }
    }
    else
    {
        // Keep the nlocal larger elements
        for (i = k = nlocal - 1, j = nlocal - 1; k >= 0; k--)
        {
            if (j == 0 || (i >= 0 && wspace[i] < relements[j]))
            {
                elements[k] = wspace[i--];
            }
            else
            {
                elements[k] = relements[j--];
            }
        }
    }
}

void main(int argc, char *argv[])
{
    int n;
    int npes;           // N processors
    int myrank;
    int nlocal;
    int *elements;      // Array that stores local elements
    int *relements;     // Araray that stores received elements
    int oddrank;
    int evenrank;
    int *wspace;
    int i;
    MPI_Status status;

    // Initialize MPI and get system information
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &npes);
    MPI_Comm_rank(MPI_COMM_WORLD, &myrank);

    n = atoi(argv[1]);
    nlocal = n/npes;

    // Allocate memory
    elements = (int *)malloc(nlocal*sizeof(int));
    relements = (int *)malloc(nlocal*sizeof(int));
    wspace = (int *)malloc(nlocal*sizeof(int));

    // Fill in the elements array with random elements
    srandom(myrank);
    for (i = 0; i < nlocal; i++)
    {
        elements[i] = random();
    }

    // sort the local elements using built-in quicksort
    qsort(elements, nlocal, sizeof(int), IncOrder);

    // Determine the rank fo the processors that myrank needs to communicate during
    // the odd and even phases of the algorithm
    if (myrank % 2 == 0)
    {
        oddrank = myrank - 1;
        evenrank = myrank + 1;
    }
    else
    {
        oddrank = myrank + 1;
        evenrank = myrank - 1;
    }
    
    // Set the ranks of the processors at the end of the linear
    if (oddrank == -1 || oddrank == npes)
        oddrank = MPI_PROC_NULL;
    if (evenrank == -1 || evenrank == npes)
        evenrank = MPI_PROC_NULL;

    // Get into the main loop of the odd-even sorting algorithm
    for (i = 0; i < npes - 1; i++)
    {
        if (i % 2 == 1)
        {
            // Odd phase
            MPI_Sendrecv(elements, nlocal, MPI_INT, oddrank, 1, relements, nlocal, MPI_INT, oddrank, 1, MPI_COMM_WORLD, &status);
        }
        else
        {
            // Even phase
            MPI_Sendrecv(elements, nlocal, MPI_INT, evenrank, 1, relements, nlocal, MPI_INT, evenrank, 1, MPI_COMM_WORLD, &status);
        }
        
        CompareSplit(nlocal, elements, relements, wspace, myrank < status.MPI_SOURCE);
    }

    free(elements); free(relements); free(wspace);
    MPI_Finalize();
}
