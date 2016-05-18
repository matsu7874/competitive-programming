// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0);
    ios::sync_with_stdio(false);
    long h,w,c[100][100],i,j,cs[101][101],max_cell,x,y;
    cin >> h >> w;
    for(i=0; i<h; ++i){
        for(j=0; j<w; ++j){
            cin >> c[i][j];
        }
    }
    for(i=0; i<h; ++i){
        for(j=0; j<w; ++j){
            if((i+j)%2 == 1){
                c[i][j] *= -1;
            }
        }
    }

    for(i=0; i<h+1; ++i){
        cs[i][0] = 0;
    }
    for(i=0; i<w; ++i){
        cs[0][i] = 0;
    }
    for(i=0; i<h; ++i){
        for(j=0; j<w; ++j){
            cs[i+1][j+1] = cs[i][j+1] + cs[i+1][j] - cs[i][j] + c[i][j];
        }
    }
    max_cell = 0;
    for(i=1; i<h+1; ++i){
        for(j=1; j<w+1; ++j){
            for(y=0; y<i+1; ++y){
                for(x=0; x<j+1; ++x){
                    if(i==y && j==x){
                        continue;
                    }
                    if(cs[i][j] - cs[y][j] - cs[i][x] + cs[y][x] == 0){
                        max_cell = max(max_cell, (i - y) * (j - x));
                    }
                }
            }
        }
    }
    cout << max_cell << "\n";

    return 0;
}
