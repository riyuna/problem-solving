#include <iostream>
#include <vector>

using namespace std;

vector<int> observation_times;
vector<int> observation_colors;

int tg, ty, tr; //time_green, time_yellow, time_red
int T, n; //total cycle time, # of observations
int tq, cq; //query time, query color

int get_shifted_color(double time, double t_initial) {
  if (time < t_initial) // if some time is < t_initial, add T once
    time += T; // now time is in [t_initial, t_initial + T[
  if (time < t_initial + tg) // green: [t_initial, t_initial + tg[
    return 'g';
  if (time < t_initial + tg + ty) // yellow: [t_initial + tg, t_initial + tg + ty[
    return 'y';
  return 'r'; // red: [t_initial + tg + ty, t_initial + T[
}

bool is_valid_t_initial(double t_initial) {
  for(int i=0; i<n; i++) {
    int time = observation_times[i];
    int color = observation_colors[i];
    int shifted_color = get_shifted_color(time, t_initial);
    if (shifted_color != color)
      return false;
  }
  return true; // all observations are consistent with t_initial
}

int main() {
  cin >> tg >> ty >> tr;
  T = tg + ty + tr;
  cin >> n;
  for (int i=0; i<n; i++) {
    int ti;
    string ci_str;
    cin >> ti >> ci_str;
    observation_times.push_back(ti % T); // time is in [0, T[
    observation_colors.push_back(ci_str[0]); // color is in ('g', 'y', 'r')
  }
  string cq_str;
  cin >> tq >> cq_str;
  cq = cq_str[0];

  const int n_samples = 10000; //to reach absolute precision 1e-3, O(1e3) samples is enough.
  int n_measurements = 0;
  int n_success = 0;
  for (int i_initial = 0; i_initial < n_samples; i_initial++) {
    double t_initial = (i_initial / (double)n_samples) * (double)T;
    // t_initial is a hypothetical start of the light-cycle
    if (!is_valid_t_initial(t_initial))
      continue;
    n_measurements++;
    if (get_shifted_color(tq, t_initial) == cq)
      n_success++;
  }
  cout << n_success / (double) n_measurements << endl;
}
