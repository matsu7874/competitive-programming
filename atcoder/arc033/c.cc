// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;

template <typename T>
class FenwickTree {
private:
    vector<T> tree;
public:
    FenwickTree(int size) : tree(size, 0) {
    }
    void add(int index, T value){
    	while(index < tree.size()) {
    		tree[index] += value;
    		index |= index + 1;
    	}
    }
    T sum(int index){
    	T res = 0;
    	--index;
    	while(index >= 0) {
    		res += tree[index];
    		index = (index & (index + 1)) - 1;
    	}
    	return res;
    }
};

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	int n = 200000 + 1;
	FenwickTree<int> ft(n);
	int q,t,x,l,r,m,rank;
	cin >> q;
	for (int i = 0; i < q; ++i) {
		cin >> t >> x;
		if(t == 1) {
			ft.add(x, 1);
		}else{
			l = 0;
			r = n;
			while (l+1 < r) {
				m = (l+r) / 2;
				rank = ft.sum(m) + 1;
				if(rank <= x) {
					l = m;
				}else{
					r = m;
				}
			}
			cout << l << endl;
			ft.add(l,-1);
		}
	}
	return 0;
}
