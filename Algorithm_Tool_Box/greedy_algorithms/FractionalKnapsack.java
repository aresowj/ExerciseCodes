import java.util.Scanner;
import java.util.Comparator;
import java.util.Collections;
import java.util.ArrayList;

public class FractionalKnapsack {
	
	private static class UnitValueComparator implements Comparator<double[]> {
		@Override
		public int compare(double[] left, double[] right) {
			if (left[0] > right[0]) {
				return -1;
			} else if (left[0] == right[0]) {
				return 0;
			} else {
				return 1;
			}
		}
	}
	
    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double value = 0.0000;
        
		double[] unitValues = new double[values.length];
		ArrayList<double[]> unitValueAndWeight = new ArrayList<double []>();
		
		for (int i = 0; i < values.length; i++) {
			double[] item = new double[] {(double) values[i] / weights[i], weights[i]};
			unitValueAndWeight.add(item);
		}
		
		Collections.sort(unitValueAndWeight, new UnitValueComparator());
		
		for (double[] item : unitValueAndWeight) {
			if (capacity <= 0) break;
			
			double weight = item[1];
			double unitValue = item[0];
			
			if (weight > capacity) {
				value += capacity * unitValue;
				capacity = 0;
			} else {
				value += weight * unitValue;
				capacity -= weight;
			}
		}

        return value;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        System.out.printf("%.4f", getOptimalValue(capacity, values, weights));
    }
} 
