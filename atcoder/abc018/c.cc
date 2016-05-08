// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;
string s[500];
int cx[500][500];

bool check(int y, int x, int k){
    for (int i = -k+1; i < k; ++i) {
        if (cx[y+i][x+k-1-abs(i)] < (k - 1 - abs(i)) * 2 + 1){
            return false;
        }
    }
    return true;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);

    int h,w,k;
    cin >> h >> w >> k;
    for(int i=0; i<h; ++i){
        cin >> s[i];
    }
    if(k * 2 - 1 > min(h, w)){
        cout << 0 << endl;
        return 0;
    }

    for(int i=0; i<h; ++i){
        for (int j=0; j<w; ++j){
            char c = s[i][j];
            if(c == 'o'){
                if (j==0){
                    cx[i][j] = 1;
                }else{
                    cx[i][j] = 1 + cx[i][j-1];
                }
            }else{
                cx[i][j] = 0;
            }
        }
    }

    int total = 0;
    for(int i=k - 1; i < h - k + 1; ++i){
        for(int j=k - 1; j< w - k + 1; ++j){
            if(check(i,j,k)){
                total += 1;
            }
        }
    }
    cout << total << endl;
    return 0;
}
