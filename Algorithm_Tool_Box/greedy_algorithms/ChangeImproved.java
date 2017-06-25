import java.util.Scanner;

public class ChangeImproved {
    private static int getChange(int m) {
        int[] coins = new int[] {10, 5, 1};
		
		int remain = m;
		int index = 0;
		int count = 0;
		
		while (remain > 0) {
			int value = coins[index];
			int used = (remain - remain % value) / value;
			count += used;
			remain = remain - value * used;
			
			index += 1;
		}
		
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        System.out.println(getChange(m));

    }
}
