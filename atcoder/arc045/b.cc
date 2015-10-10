#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

long N,M;
long cs[300001]={0},L[100000]={0},s[100000],t[100000];
vector<long> vc;
int main() {
    scanf("%ld %ld", &N, &M);
    for(long i=0; i<M; i++){
        scanf("%ld %ld", &s[i], &t[i]);
        s[i]--;
        t[i]--;
        cs[s[i]]++;
        cs[t[i]]--;
    }
    for(long i=1; i<N; i++){
        cs[i]+=cs[i-1];
    }

    long cnt = 0;
    for(long i=0; i<N; i++){
        if(cs[i]>=2){
            cnt++;
            L[i] = cnt;
        }else{
            cnt = 0;
        }
    }
    for(long i=0; i<M; i++){
        if(L[t[i]] >= t[i] - s[i] + 1){
            vc.push_back(i+1);
        }
    }
    long sz=vc.size();
    printf("%ld\n",sz);
    for(long i=0; i<sz; i++){
        printf("%ld\n",vc[i]);
    }
    return 0;
}
