import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class fran_bolts_overflow {

	/*
	1000
	9
	1 2
	1 1000
	1 2
	1 1000
	1 2
	1 1000
	1 2
	1 1000
	1 1

	1000000000
	9
	1 2
	1 1000
	1 2
	1 1000
	1 2
	1 1000
	1 2
	1 1000
	1 1

	1000
	9
	1 2
	1 10
	1 2
	1 10
	1 2
	1 10
	1 2
	1 10
	1 1

	 */
	static int B, k;
	static int[][] boltsPackage;
	static long[][] boltsReality;

	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		B              = reader.nextInt();
		k              = reader.nextInt();
		boltsPackage   = new int[k][];
		boltsReality   = new long[k][];
		for(int i = 0; i < k; i++) {
			int l           = reader.nextInt();
			boltsPackage[i] = new int[l];
			for(int j = 0; j < l; j++) { boltsPackage[i][j] = reader.nextInt(); }
		}
		solve();
		reader.close();
	}

	static void solve() {
		for(int i = 0; i < boltsPackage.length; i++) {
			solveCompany(i);
			// System.err.println(Arrays.toString(boltsReality[i]));
		}
		int min = Integer.MAX_VALUE;
		for(int i = 0; i < boltsPackage.length; i++) {
			for(int j = 0; j < boltsPackage[i].length; j++) {
				if(boltsReality[i][j] >= B && boltsPackage[i][j] < min) {
					min = Math.min(min, boltsPackage[i][j]);
				}
			}
		}
		if(min == Integer.MAX_VALUE)
			System.out.println("impossible");
		else
			System.out.println(min);
	}

	static void solveCompany(int i) {
		Arrays.sort(boltsPackage[i]);
		boltsReality[i] = new long[boltsPackage[i].length];
		if(i == 0) {
			for(int j = 0; j < boltsPackage[i].length; j++) {
				boltsReality[i][j] = boltsPackage[i][j];
			}
		} else {
			ArrayList<Long> minbolts = new ArrayList<>();
			minbolts.add(0l);
			int v = 1;
			while(true) {
				long min = Long.MAX_VALUE;
				for(int j = 0; j < boltsPackage[i - 1].length; j++) {
					if(v - boltsPackage[i - 1][j] >= 0 &&
					   minbolts.get(v - boltsPackage[i - 1][j]) != Long.MAX_VALUE) {
						min = Math.min(min, minbolts.get(v - boltsPackage[i - 1][j]) +
						                        boltsReality[i - 1][j]);
						break;
					}
				}
				minbolts.add(min);
				if(v >= boltsPackage[i][boltsPackage[i].length - 1] && min != Long.MAX_VALUE) break;
				v++;
			}
			int j = 0;
			v     = 0;
			while(j < boltsPackage[i].length && v < minbolts.size()) {
				if(minbolts.get(v) != Long.MAX_VALUE && v >= boltsPackage[i][j]) {
					boltsReality[i][j] = minbolts.get(v);
					j += 1;
				} else {
					v++;
				}
			}
		}
	}
}
