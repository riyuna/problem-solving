import java.util.*;

/*
Copied Timon's code for this
 */

public class JoshuaBills {
    Scanner s = new Scanner(System.in);

    public static void main(String[] args) {
        (new JoshuaBills()).solve();
    }

    void solve() {
        int M = s.nextInt();
        int N = s.nextInt();

        int[] C = new int[M];

        while(N-- > 0){
            int a = s.nextInt();
            int b = s.nextInt();
            int p = s.nextInt();
            C[a] -= p;
            C[b] += p;
        }

        int[] dp = new int[1 << M];
        for (int m = 1; m < (1<<M); ++m) {
            int sum = 0;
            for (int i = 0; i < M; ++i)
                if (((m>>i) & 1) != 0) {
                    sum += C[i];
                    dp[m] = Integer.max(dp[m], dp[m & ~(1 << i)]);
                }
            if (sum == 0) {
                ++dp[m];
            }
        }

        System.out.println(M - dp[dp.length-1]);
    }
}
