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

# for i in range(10):
#     arr.add(i)

# print(arr.SumOverRange(2,5)) # prints the sum of 2+3+4=9. 5 is excluded

arr.add(3)
arr.add(4)
arr.add(5)
arr.add(10)
arr.add(8)
arr.add(9)
arr.add(25)
arr.add(30)

print(arr.SumOverRange(2,6))