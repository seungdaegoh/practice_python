#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
#include <map>
#include <iterator>
#include <unistd.h>
#include <math.h>

using namespace std;

int N,K;

int main(int argc,char *argv[])
{
    std::vector<long> vec;
    scanf("%d %d", &N,&K);

    int temp;
    for(int i = 0 ; i < N ; i++){
        scanf("%d",&temp);
        vec.push_back(temp);
    }
    double min = -1.0;
    double sd = 0.0;
    long squareSum = 0;
    long sum = 0;

    for(int k = K ; k <= N ; k++){
        squareSum = 0;
        sum = 0;
        for(int j = 0 ; j < k ; j++){
            squareSum += (long)vec[j] * vec[j];
            sum += vec[j];
        }
        double mean = (double)sum / k;
        sd = sqrt(((double) squareSum / k ) - (mean * mean ));
        if(min == -1.0){ min = sd; }
        if(sd < min) { min = sd; }

        for(int i = 1 ; i < (N -k +1) ; i++){
            squareSum -= (long)vec[i-1] * vec[i-1];
            squareSum += (long)vec[i+k-1] * vec[i+k-1];
            sum -= vec[i-1];
            sum += vec[i+k-1];
            mean = (double)sum / k;
            sd = sqrt(((double)squareSum / k ) - (mean * mean));
            if(sd < min) { min = sd; }
        }
    }

    printf("%.7lf\n",min);
    return 0;
}
