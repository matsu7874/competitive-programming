class WeightedUnionFind:
    """
    重み付きUnionFind

    """
    root_position = 0

    def __init__(self, size: int):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.size = size
        self.parent = [-1] * size
        self.weight = [WeightedUnionFind.root_position] * size

    def find(self, x: int) -> (int, int):
        """
        xを含む集合の代表とxの代表からの位置を求める
        """
        if self.parent[x] < 0:
            return x, self.weight[x]
        root, weight = self.find(self.parent[x])
        self.parent[x] = root
        self.weight[x] += weight
        return root, self.weight[x]

    def union(self, x: int, y: int, weight: int) -> bool:
        """
        xを含む集合とyを含む集合を併合する
        `weight[x] + weight = weight[y]`になるように辺に重みをもたせる。
        xとyがすでに同じ集合に含まれている場合Falseを返す。
        """
        root_x, weight_x = self.find(x)
        root_y, weight_y = self.find(y)

        if root_x == root_y:
            return False

        if self.parent[root_x] >= self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
            self.weight[root_y] = weight_x + weight - weight_y
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
            self.weight[root_x] = weight_y - weight - weight_x

        return True


def main():
    n, m = map(int, input().split())
    wut = WeightedUnionFind(n)
    for _ in range(m):
        l, r, d = map(int, input().split())
        l -= 1
        r -= 1
        merged = wut.union(l, r, d)
        if not merged:
            root_l, weight_l = wut.find(l)
            root_r, weight_r = wut.find(r)
            if root_l != root_r or weight_l + d != weight_r:
                return False
    return True


if __name__ == '__main__':
    result = main()
    print('Yes' if result else 'No')
