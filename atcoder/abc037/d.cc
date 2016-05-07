#include<iostream>
#include<queue>
#include<utility>
using namespace std;

int h,w;
long a[1000][1000];
long route[1000][1000];

long search(int y, int x){
    if (route[y][x] > 0){
        return route[y][x];
    }
    long long local = 1;
	int dy[4]={1,0,-1,0},dx[4]={0,1,0,-1};
	for(int i=0;i<4;++i){
        int ny = y+dy[i], nx=x+dx[i];
        if(0<=ny && ny<h && 0<= nx && nx < w){
            if(a[ny][nx] > a[y][x]){
                local += search(ny,nx);
            }
        }
	}
    route[y][x] = local % 1000000007;
    return route[y][x];

}

int main(){
    long total = 0;
    cin >> h >> w;
    for(int i=0; i<h; ++i){
        for(int j=0; j<w; ++j){
            cin >> a[i][j];
            route[i][j] = 0;
        }
    }
    for(int i=0; i<h; ++i){
        for(int j=0; j<w; ++j){
            total = (total + search(i, j)) % 1000000007;
        }
    }
    cout << total << endl;
}
