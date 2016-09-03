import java.util.*;
import java.io.*;

public class MaxPairwiseProduct {
    static long getMaxPairwiseProduct(long[] numbers) {
        int n = numbers.length;
		Arrays.sort(numbers);
        return numbers[n-1] * numbers[n-2];
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        long n = scanner.nextLong();
        long[] numbers = new long[(int)n];
        for (int i = 0; i < (int)n; i++) {
            numbers[i] = scanner.nextLong();
        }
        System.out.println(getMaxPairwiseProduct(numbers));
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

}