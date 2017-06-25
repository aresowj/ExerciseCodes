import java.util.*;

public class Tester {
	private static long maxDotProduct(int[] a, int[] b) {
        //write your code here
        long result = 0;
		
		Arrays.sort(a);
		Arrays.sort(b);
		
        for (int i = 0; i < a.length; i++) {
            result += a[i] * b[i];
        }
		
        return result;
    }
	
	private static long maxDotProductNaive(int[] a, int[] b) {
        //write your code here
        long result = 0;
		
		Arrays.sort(a);
		Arrays.sort(b);
		
        for (int i = 0; i < a.length; i++) {
            result += a[i] * b[i];
        }
		
        return result;
    }
	
	public static int randInt(int min, int max) {
		Random rand = new Random();

		// nextInt is normally exclusive of the top value,
		// so add 1 to make it inclusive
		int randomNum = rand.nextInt((max - min) + 1) + min;

		return randomNum;
	}
	
	public static int getRandInt() {
		return randInt(-100000, 100000);
	}
	
	public static void generateResult() {
		int n = randInt(1, 100);
        int[] a = new int[n];
		int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = randInt(-100000, 100000);
            b[i] = randInt(-100000, 100000);
        }
        long result1 = maxDotProduct(a, b);
		
        System.out.println(result1);
	}

    public static void main(String[] args) {
        for (int i = 0; i < 100; i++) {
			generateResult();
		}
    }
}
