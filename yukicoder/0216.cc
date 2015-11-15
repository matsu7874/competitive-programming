#include <bits/stdc++.h>
using namespace std;
typedef signed long long ll;

int main()
{
    int n; cin>>n;
    vector<int> a(n), b(n), c(101);
    for(int& v: a){
        cin>>v;
    }
    for(int& v: b){ cin>>v;}

    for(int i=0;i<n;++i) c[b[i]]+=a[i];
    cout<<(*max_element(begin(c), end(c))==c[0] ? "YES" : "NO")<<endl;
}
