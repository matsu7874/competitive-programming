#include <cstdio>
#include <vector>

using namespace std;

class RMQ{
  private:
    static const int MAX_N = 1 << 18;
    int n, dat[2*MAX_N -1];
    //[a,b)の最小値を返す
    //kは節点の番号l,rはその節点が[l,r)を保持している
    int rec(int a,int b,int k,int l,int r){
      if(b <= l || r <= a){
        return -1;
      }

      if(a<=l && r<=b){
        return dat[k];
      }else{
        int rl = rec(a,b,2*k+1,l,(l+r)/2);
        int rr = rec(a,b,2*k+2,(l+r)/2,r);
        return max(rl,rr);
      }
    }

  public:
    void init(int n_){
      n=1;
      while(n < n_) n*=2;

      for(int i=0;i<2*n-1;i++){
      dat[i] = -1;
      }
    }

    //kをaに変更
    void update(int k, int a){
      int reaf = k+n-1;
      dat[reaf]=a;
      while(reaf>0){
        reaf = (reaf-1)/2;
        dat[reaf]=max(dat[reaf*2+1],dat[2*reaf+2]);
      }
    }

    //query[a,b]の範囲内の最小値を返す
    int query(int a,int b){
      return rec(a,b+1,0,0,n);
    }
};


int main(void){
    long N;
    scanf("%ld",&N);
    long LIMIT =100002;
    long min_a = N;
    long A[LIMIT]={0},B[LIMIT]={0},S[LIMIT]={0},T[LIMIT]={0};
    for(long i=0;i<N;i++){
        long s,t;
        scanf("%ld %ld",&s,&t);
        S[i]=s;
        T[i]=t;
        B[s] += 1;
        B[t] -= 1;
    }
    for(long i=1; i<LIMIT; i++){
        A[i] = A[i-1] + B[i];
    }
    RMQ r;
    r.init(LIMIT);
    for(long i=0; i<LIMIT; i++){
        r.update(i,A[i]);
    }
    for(long i=0; i<N;i++){
        long max_a = max(max(r.query(1, S[i] - 1), r.query(S[i],T[i]-1) - 1), r.query(T[i], 100001));
        min_a = min(min_a, max_a);
    }
    printf("%ld\n",min_a);

    return 0;
}
