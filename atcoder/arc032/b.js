function UnionFind(size){
  this._values = new Array(size);
  this._values.fill(-1);
}

UnionFind.prototype = {
  find: function(x){
    while(this._values[x] >= 0){
      x = this._values[x];
    }
    return x;
  },
  union: function(x,y){
    px = this.find(x);
    py = this.find(y);
    if (px !== py){
      if(this._values[px] > this._values[py]){
        this._values[px] += this._values[py];
        this._values[py] = px;
      }else{
        this._values[py] += this._values[px];
        this._values[px] = py;
      }
    return this._values[px];
    }
  },
  count: function(){
    var group = 0;
    for(var i = 0; i<this._values.length; ++i){
      if(this._values[i] < 0){
        group += 1;
      }
    }
    return group;
  }
};


function main(input){
  var rows = input.split("\n");
  var n,m;
  n = parseInt(rows[0].split(" ")[0],10);
  m = parseInt(rows[0].split(" ")[1],10);
  var uf = new UnionFind(n);
  for(var i=0; i<m; i++){
    var a,b;
    a = parseInt(rows[i+1].split(" ")[0], 10) - 1;
    b = parseInt(rows[i+1].split(" ")[1], 10) - 1;
    uf.union(a,b);
  }
  console.log(uf.count()-1);
}

main(require("fs").readFileSync("/dev/stdin", "utf8"));
