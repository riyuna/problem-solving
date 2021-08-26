#include <vector>
#include <iostream>
#include <limits>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <numeric>

class Problem
{
public:
        static std::vector<double> logsoftmax(std::vector<double> activation) {
            // TODO implement this
            double mxm = DBL_MIN;
            double total=0.0;
            int size_of_act = activation.size();
            for(int i=0;i<size_of_act;i++){
                if(mxm<activation[i])mxm=activation[i];
            }
            for (int i=0;i<size_of_act;i++)total+=exp(activation[i]-mxm);
            total = log(total)+mxm;
            for (int i=0;i<size_of_act;i++)activation[i]-=total;
            return activation;
        }

};

#ifndef RunTests
int main()
{
    std::vector<double> activation =  {-3.44, 1.16, -0.81, 3.91};
    auto lsoftmax = Problem::logsoftmax(activation);
    std::cout << setprecision(10);
    for (auto x: lsoftmax) {
        std::cout << x << std::endl;
    }
    return 0;
}
#endif