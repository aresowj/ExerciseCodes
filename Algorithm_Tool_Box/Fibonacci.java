import java.util.Scanner;

public class Fibonacci {
  private static long calc_fib(int n) {
	if(n < 1) return 0;
	
	int fibs1 = 0;
	int fibs2 = 1;
	int current = 2;
	int fibsCurrent = fibs1 + fibs2;
	
	while(current <= n) {
		fibsCurrent = fibs1 + fibs2;
		fibs1 = fibs2;
		fibs2 = fibsCurrent;
		current += 1;
	}

    return fibsCurrent;
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}
