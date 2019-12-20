#include <stdio.h>
#include <math.h>

#define MAX_N 500

int N, K;
int nLike[MAX_N];

double get_variance(int st_i, int ed_i)
{
    int nCnt = (ed_i - st_i);
    //printf("st_i, ed_i, cnt= %d, %d, %d\n", st_i, ed_i, nCnt);

    int sum = 0;
    int j;
    for (j = st_i; j < ed_i; j++) {
//#        print("[", nLike[j], "]", end='');
        sum += nLike[j];
	}

    double average = (double)sum/ nCnt;

    double t_var = 0.0;
    for (j = st_i; j < ed_i; j++) {
        double _val = ((double)nLike[j] - average	);
        t_var += (_val * _val);
    }

    double var = t_var / nCnt;

//#    print("\nVAR=", var, "\n")
    return var;
}

int main(void)
{
	int i, k;
	scanf("%d %d", &N, &K);
	for (i = 0; i < N; i++) {
		scanf("%d", &nLike[i]);
	}

	double min_var = -1;
	for (k = K; k <= N; k++) {
		for (i = 0; i < (N-k+1); i++) {
			//printf("k= %d idx=%d \n", k, i);
			double r_val = get_variance(i, i+k);
			if (min_var == -1 || min_var > r_val)
				min_var = r_val;

		}
	}
	//printf("%lf\n", min_var);
	printf("%.7lf\n", sqrt(min_var));
	//print(sqrt(min_var));
}



