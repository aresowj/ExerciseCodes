import java.util.*;

public class LargestNumber {
	private static class FirstDigitComparator implements Comparator<String> {
		@Override
		public int compare(String left, String right) {
			int leftFirst = Integer.parseInt(left + right);
			int rightFirst = Integer.parseInt(right + left);
			
			if (leftFirst > rightFirst) {
				return -1;
			} else if (leftFirst == rightFirst) {
				return 0;
			} else {
				return 1;
			}
		}
	}
	
    private static String largestNumber(String[] a) {
        //write your code here
        String result = "";
		
		Arrays.sort(a, new FirstDigitComparator());
		
        for (int i = 0; i < a.length; i++) {
            result += a[i];
        }
		
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] a = new String[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.next();
        }
        System.out.println(largestNumber(a));
    }
}
