import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Scanner;

class Package {
  int size, actual_size;

  Package(int s, int a) {
    size = s;
    actual_size = a;
  }
}

public class BuyingBolts_HarryACC {

  static PriorityQueue<Package> queue = new PriorityQueue<Package>((a, b) -> b.size - a.size);
  static PriorityQueue<Integer> target = new PriorityQueue<Integer>();
  static ArrayList<ArrayList<Package>> used_packages;

  static void find_target(int i) {
    while (!target.isEmpty()) {
      int t = target.peek();
      Package p = queue.remove();
      if (p.size > t) {
        target.remove();
        used_packages.get(i).add(new Package(t, p.actual_size));
      }
      for (Package q : used_packages.get(i - 1))
        queue.add(new Package(p.size + q.size, p.actual_size + q.actual_size));
    }
  }

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    int B = sc.nextInt();
    int k = sc.nextInt();

    used_packages = new ArrayList<ArrayList<Package>>(k);
    for (int i = 0; i < k; i++)
      used_packages.add(new ArrayList<Package>());

    for (int i = 0; i < k; i++) {
      int l = sc.nextInt();

      if (i == 0) {
        for (int j = 0; j < l; j++) {
          int s = sc.nextInt();
          used_packages.get(0).add(new Package(s, s));
        }
        continue;
      }

      for (int j = 0; j < l; j++) target.add(sc.nextInt());
      queue.add(new Package(0, 0));
      find_target(i);
    }

    int smallest_size = 1000000000;
    Package best = new Package(-1, -1);
    int best_index = -1;

    for (int i = 0; i < k; i++) {
      ArrayList<Package> al = used_packages.get(i);
      for (Package p : al)
        if (p.actual_size >= B && p.size < smallest_size) {
          smallest_size = p.size;
          best = p;
          best_index = i;
        }
    }
    if (best_index == -1)
      System.out.println("impossible");
    else
      System.out.println(best.size);
    // System.out.println(best.size + " " + best.actual_size);
  }
}
