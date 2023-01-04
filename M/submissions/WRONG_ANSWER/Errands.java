import java.util.*;

/*
Copied Timon's code for this
Joshua
TODO: debug and make it work, like Timon's code...
 */

public class Errands {
    Scanner s = new Scanner(System.in);

    public static void main(String[] args) {
        (new Errands()).solve();
    }

    void solve() {
        int n = s.nextInt(), xm = s.nextInt(), ym = s.nextInt(), xM = s.nextInt(), yM = s.nextInt();

        if (xm > xM) {
            int t = xM;
            xM = xm;
            xm = t;
            t = ym;
            yM = ym;
            ym = t;
        }

        int m = ym <= yM ? 1 : -1;
        ym *= m;
        yM *= m;

        // array of pairs
        List<int[]> E = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int x = s.nextInt(), y = s.nextInt();
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
