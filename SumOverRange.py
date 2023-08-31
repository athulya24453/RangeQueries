class SummingArray:
    def __init__(self):
        self.sum = []
        self.arr = []
        self.ind = 0

    def add(self, e):
        self.arr.append(e)
        self.ind += 1
        if self.ind == 1:
            self.sum.append(e)
        else:
            cur_sum = self.sum[self.ind-2] + e
            self.sum.append(cur_sum)

    def remove(self):
        self.arr.pop()
        self.sum.pop()

    def SumOverRange(self, i, j):
        return self.sum[j-1] - self.sum[i-1]

arr = SummingArray()

for i in range(10):
    arr.add(i)

print(arr.SumOverRange(2,5))

