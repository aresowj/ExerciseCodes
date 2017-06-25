import java.util.Scanner;

public class FibonacciLastDigit {
  private static long calc_fib(int n) {
	if(n < 1) return 0;
	
	int fibs1 = 0;
	int fibs2 = 1;
	int current = 2;
	int lastDigit = (fibs1 + fibs2) % 10;
	
	while(current <= n) {
		lastDigit = (fibs1 + fibs2) % 10;
		fibs1 = fibs2;
		fibs2 = lastDigit;
		current += 1;
	}

    return lastDigit;
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    System.out.println(calc_fib(n));
  }
}
