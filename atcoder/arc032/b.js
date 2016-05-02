function UnionFind(size){
  this._values = new Array(size);
  for(var i=0; i<size; ++i){
      this._values[i] = -1;
  }
}

UnionFind.prototype = {
  find: function(x){
    while(this._values[x] >= 0){
        if(this._values[this._values[x]] >= 0){
            this._values[x] = this._values[this._values[x]];
        }
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
  countGroup: function(){
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
  var tmp = rows[0].split(" ");
  n = parseInt(tmp[0],10);
  m = parseInt(tmp[1],10);
  var uf = new UnionFind(n);
  for(var i=0; i<m; i++){
    var a,b;
    tmp = rows[i+1].split(" ");
    a = parseInt(tmp[0], 10) - 1;
    b = parseInt(tmp[1], 10) - 1;
    uf.union(a,b);
  }
  console.log(uf.countGroup()-1);
}

main(require("fs").readFileSync("/dev/stdin", "utf8"));
