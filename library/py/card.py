class Card:

    def __init__(self, suit, rank):
        self.suit = 'SHDC'[suit]
        self.rank = rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank

    def __str__(self):
        s = self.suit + str(self.rank)
        return s

if __name__ == '__main__':
    cs = [Card(3, 6), Card(2, 3), Card(0, 3), Card(3, 2), Card(1, 6)]
    print(*cs,sep=',')
    cs.sort()
    print(*cs,sep=',')
