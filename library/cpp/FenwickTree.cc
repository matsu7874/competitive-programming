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
