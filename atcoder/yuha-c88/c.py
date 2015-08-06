class UnionFind:
    def __init__(self, size):
        # 負の値はルート (集合の代表) で集合の個数
        # 正の値は次の要素を表す
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    # 併合
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] >= self.table[s2]:
                # 小さいほうが個数が多い
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False


def main():
    N = int(input())
    S = [input() for i in range(N)]
    M = [input().split() for i in range(N)]
    T = UnionFind(N)
    for i in range(N):
        j = S.index(M[i][0])
        message = M[i][3]
        if message == 'good':
            T.union(i,j)
    teams = [[i,0,set()] for i in range(N)]
    for i in range(N):
        teams[T.find(i)][1] += 1
    for i in range(N):
        message = M[i][3]
        if message == 'bad':
            j = T.find(S.index(M[i][0]))
            if j == T.find(i):
                print('No answers')
                exit()
            else:
                teams[T.find(i)][2].add(j)
                teams[j][2].add(T.find(i))
    for i in range(N):
        for team in teams[T.find(i)][2]:
            for t in teams[T.find(team)][2]:
                T.union(i,t)
    teams = [[i,0,set()] for i in range(N)]
    for i in range(N):
        teams[T.find(i)][1] += 1
    for i in range(N):
        message = M[i][3]
        if message == 'bad':
            j = T.find(S.index(M[i][0]))
            if j == T.find(i):
                print('No answers')
                exit()
            else:
                teams[T.find(i)][2].add(j)
                teams[j][2].add(T.find(i))
    # print(teams)
    good_teams = set()
    for t in teams:
        if t[1] == 0:
            continue
        if sum([teams[i][1] for i in t[2]]) < t[1]:
            # print(t[0], 'is good_teams, *1')
            good_teams.add(t[0])
        elif sum([teams[i][1] for i in t[2]]) == t[1]:
            first = '~'
            for i in range(N):
                if S[i]<first and (T.find(i) == t[0] or T.find(i) in t[2]):
                    first = S[i]
            if T.find(S.index(first)) == t[0]:
                # print(t[0], 'is good_teams, *2',first,T.find(S.index(first)), t[0])
                good_teams.add(t[0])
    goods = []
    for i in range(N):
        if T.find(i) in good_teams:
            goods.append(S[i])
    goods.sort()
    for g in goods:
        print(g)






if __name__ == '__main__':
    main()
