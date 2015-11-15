#include <vector>
#include <map>
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

#define lld long long int

int main(){
    lld N;
    scanf("%lld",&N);
    vector<pair<lld, lld>> p;
    for(lld i=0;i<N;i++){
        lld s,c;
        scanf("%lld %lld",&s,&c);
        lld t = s+c-1;
        lld j=0;
        while (true){
            if(j <= p.size()){
                break;
            }
            if (p[j].first <= s && s <= p[j].second){
                t =  t + p[j].second - s + 1;
                s = p[j].first;
                p.erase(p.begin()+j);
                continue;
            }else if (s < p[j].first && p[j].first <= t){
                t = t + p[j].second - p[j].first + 1;
                p.erase(p.begin()+j);
                continue;
            }else if (t < p[j].first){
                break;
            }
            j += 1;
        }
        p.push_back(pair<lld, lld>(s, t));
        sort(p.begin(), p.end());
        printf("%lld\n",t);
    }
    return 0;
}
