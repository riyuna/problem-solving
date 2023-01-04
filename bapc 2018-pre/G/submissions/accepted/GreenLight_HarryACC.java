import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class GreenLight_HarryACC {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int green_time = sc.nextInt();
		int yellow_time = sc.nextInt();
		int red_time = sc.nextInt();
		
		int total_time = green_time + yellow_time + red_time;
		
		int n = sc.nextInt();
		
		ArrayList<Integer> green = new ArrayList<Integer>();
		ArrayList<Integer> yellow = new ArrayList<Integer>();
		ArrayList<Integer> red = new ArrayList<Integer>();
		
		for(int i = 0; i < n; i++)
		{
			int t = sc.nextInt();
			String s = sc.nextLine();
			char u = s.charAt(1);
			if(u == 'g') { green.add(t % total_time); }
			if(u == 'y') { yellow.add(t % total_time); }
			if(u == 'r') { red.add(t % total_time); }			
		}
		
		Collections.sort(red);
		Collections.sort(green);
		Collections.sort(yellow);
		
		int target_time = sc.nextInt() % total_time;
		char target_colour = sc.nextLine().charAt(1);
		
		//Find the "first" green.
		Boolean done = false;
		int first_green = -1;
		for(int i = 0; i < red.size() && !done; i++)
		{
			int maybe_last = red.get(i);
			int next = red.get((i + 1) % red.size());
			
			if(next < maybe_last) next += total_time;
			
			for(int j = 0; j < green.size() && !done; j++)
			{
				first_green = green.get(j);
				if(first_green < maybe_last) first_green += total_time;
				if(first_green > maybe_last && first_green < next) done = true;
				first_green = first_green % total_time;				
			}
		}
		
		// We set the first green observation to zero.
		for(int i = 0; i < red.size(); i++)
			red.set(i, (red.get(i) - first_green + total_time) % total_time);
		
		for(int i = 0; i < green.size(); i++)
			green.set(i, (green.get(i) - first_green + total_time) % total_time);
		
		for(int i = 0; i < yellow.size(); i++)
			yellow.set(i, (yellow.get(i) - first_green + total_time) % total_time);
				
		Collections.sort(red);
		Collections.sort(green);
		Collections.sort(yellow);
		
		
		int first_yellow = yellow.get(0);
		int first_red = red.get(0);		
		
		
		
		// How much do we need to go to the left to make every observation fit?
		int left_shift = Math.max(0, Math.max(green_time - first_yellow, green_time + yellow_time - first_red));
		
		for(int i = 0; i < red.size(); i++)
			red.set(i, (red.get(i) + left_shift) % total_time);
		
		for(int i = 0; i < green.size(); i++)
			green.set(i, (green.get(i) + left_shift) % total_time);
		
		for(int i = 0; i < yellow.size(); i++)
			yellow.set(i, (yellow.get(i) + left_shift) % total_time);
		
		
		
		int last_green = green.get(green.size() - 1);
		int last_yellow = yellow.get(yellow.size() - 1);
		int last_red = red.get(red.size() - 1);
		
		
		// How much can we go to the right?		
		int room = Math.min(Math.min(green_time - last_green, green_time + yellow_time - last_yellow), total_time - last_red) - 1;
		
		
		target_time = (target_time - first_green + left_shift + total_time) % total_time;
		int l_certain = 0, r_certain = 0;
		int l_poss = 0, r_poss = 0;
		
		if(target_colour == 'g')
		{
			l_certain = 0;
			l_poss = -room;
			r_certain = green_time - room - 1;
			r_poss = green_time - 1;
			
			if(target_time > r_poss) 
				target_time -= total_time;
		}		
		else if(target_colour == 'y')
		{ 
			l_certain = green_time;
			l_poss = green_time - room;
			r_certain = green_time + yellow_time - room - 1;
			r_poss = green_time + yellow_time - 1;
		}
		else if(target_colour == 'r')
		{
			l_certain = green_time + yellow_time;
			l_poss = green_time + yellow_time - room;
			r_certain = total_time - room - 1;
			r_poss = total_time - 1;
			
		}
		if(target_time >= l_poss && target_time <= r_poss)
		{
			if(target_time >= l_certain && target_time <= r_certain)
				System.out.println(1);
			else if (target_time < l_certain) 
			{
				double ans = 1 - ((l_certain - target_time) / (room + 1.0d));
				System.out.println(ans);
			}
			else 
			{
				double ans = 1 - ((target_time - r_certain) / (room + 1.0d));
				System.out.println(ans);
			}
		}
		else System.out.println(0);
		
		
	}

}
