import java.util.Scanner;

public class Change {
    private static int getChange(int m) {
        int[] coins = new int[] {10, 5, 1};
		
		int remain = m;
		int index = 0;
		int count = 0;
		
		while (remain > 0) {
			int value = coins[index];
			
			if (remain < value) {
				// coin value too large to fill
				index += 1;
				continue;
			} else {
				remain = remain - value;
				count += 1;
			}
		}
		
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));

    }
}
