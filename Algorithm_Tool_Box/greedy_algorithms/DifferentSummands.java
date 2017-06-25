import java.util.*;

public class DifferentSummands {
    private static List<Integer> optimalSummands(int n) {
        List<Integer> summands = new ArrayList<Integer>();
        
		int remain = n;
		int summand = 1;
		
		while (remain > 0) {
			if (remain - summand <= summand) {
				summand = remain;
			}
			
			summands.add(summand);
			remain -= summand;
			summand += 1;
		}
		
        return summands;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> summands = optimalSummands(n);
        System.out.println(summands.size());
        for (Integer summand : summands) {
            System.out.print(summand + " ");
        }
    }
}
