function FenwickTree(size) {
    this._size = size;
    this._tree = new Array(this._size);
    for (var i = 0; i < this._size; ++i) {
        this._tree[i] = 0;
    }
}

FenwickTree.prototype.add = function (index, value) {
    for(var x = index; x < this._size; x |= x+1){
        this._tree[x] += value;
    }
};

FenwickTree.prototype.sum = function (index) {
    var ret = 0;
    for(var x = index-1; x>= 0; x = (x & (x + 1)) - 1){
        ret += this._tree[x];
    }
    return ret;
};

function main(input) {
    var n = 200000 + 1;
    var ft = new FenwickTree(n);
    var rows = input.split("\n");
    var q = parseInt(rows[0], 10);
    var t, x, tmp, l, r, m, rank;
    for(var i=1; i<=q; ++i){
        tmp = rows[i].split(" ");
        t = tmp[0];
        x = parseInt(tmp[1], 10);
        if(t === "1"){
            ft.add(x, 1);
        }else{
            l = 0;
            r = n;
            while(l + 1 < r){
                m = Math.floor((l + r) / 2);
                rank = ft.sum(m) + 1;
                if(rank <= x){
                    l = m;
                }else{
                    r = m;
                }
            }
            console.log(l);
            ft.add(l, -1);
        }
    }
}

main(require("fs").readFileSync("/dev/stdin", "utf8"));
