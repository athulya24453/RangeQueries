class Duplicates:
    def __init__(self):
        self.t = []
        self.p = {}
        self.q = []
        self.ind = 0

    def add(self, e):
        self.t.append(e)
        self.ind += 1

        if e in self.p:
            self.p[e] += 1

        else: 
            self.p[e] = -1

        if self.ind == 1:
            self.q.append(-1)

        elif self.p[e] > self.q[self.ind-2]:
            self.q.append(self.p[e])
        
        else:
            self.q.append(-1)

    def n_dup(self, i, j):
        return self.q[j-1]
    
arr = Duplicates()

arr.add(0)
arr.add(3)
arr.add(3)
arr.add(1)
arr.add(0)
arr.add(5)


