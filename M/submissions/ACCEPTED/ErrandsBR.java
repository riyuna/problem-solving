import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.TreeSet;

/*
Copied Timon's code for this
Joshua
 */

public class ErrandsBR {
    private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        (new ErrandsBR()).solve();
    }

    void solve() throws IOException {
        String[] words = br.readLine().split("\\s");
        int n = Integer.parseInt(words[0]);
        words = br.readLine().split("\\s");
        int xm = Integer.parseInt(words[0]), ym = Integer.parseInt(words[1]);
        int xM = Integer.parseInt(words[2]), yM = Integer.parseInt(words[3]);

        if (xm > xM) {
            int t = xM;
            xM = xm;
            xm = t;
            t = yM;
            yM = ym;
            ym = t;
        }

        int m = ym <= yM ? 1 : -1;
        ym *= m;
        yM *= m;

        // array of pairs
        List<int[]> E = new ArrayList<>(n);

        for (int i = 0; i < n; i++) {
            words = br.readLine().split("\\s");
            int x = Integer.parseInt(words[0]), y = Integer.parseInt(words[1]);
            y *= m;
            if (x < xm || x > xM || y < ym || y > yM) continue;
            E.add(new int[]{x, y});
        }

        // sort lexicographically
        Comparator<int[]> comp = (o1, o2) -> {
            int r = Integer.compare(o1[0], o2[0]);
            if (r != 0) return r;
            return Integer.compare(o1[1], o2[1]);
        };
        E.sort(comp);

        int c = 0;
        TreeSet<int[]> level = new TreeSet<>(comp);
        for (int[] xy : E) {
            int[] it = level.ceiling(new int[]{xy[1], 1000000000});
            if (it != null) {
                level.remove(it);
            }
            level.add(new int[]{xy[1], c++});
        }

        System.out.println(level.size());
    }
}