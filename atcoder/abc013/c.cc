// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    long long N,H,A,B,C,D,E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    long long l,m,r,normal, simple, fast;
    long long money;
    l = -1;
    r = C * N;
    while (l+1 < r){
        m = (l+r)/2;
        bool canAlive = false;
        for(normal = m/A; normal >= 0; --normal){
            simple = (m-A*normal) / C;
            fast = N - normal - simple;
            if (H + B*normal + D*simple - E*fast > 0){
                canAlive = true;
                break;
            }
        }
        if (canAlive){
            r = m;
        }else{
            l = m;
        }
    }
    cout << r << endl;

    return 0;
}
