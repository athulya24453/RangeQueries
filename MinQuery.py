MAX = 500

lookup = [[0 for j in range(MAX)]
			for i in range(MAX)]

class Query:
	
	def __init__(self, L, R):
		
		self.L = L
		self.R = R

def preprocess(arr, n):

	for i in range(n):
		lookup[i][i] = i;

	for i in range(n):
		for j in range(i + 1, n):

			if (arr[lookup[i][j - 1]] < arr[j]):
				lookup[i][j] = lookup[i][j - 1];
			else:
				lookup[i][j] = j;

def RMQ(arr, n, q, m):

	preprocess(arr, n);

	for i in range(m):

		L = q[i].L
		R = q[i].R;

		print("Minimum of [" + str(L) + ", " +
			str(R) + "] is " +
			str(arr[lookup[L][R]]))

if __name__ == "__main__":
	
	a = [7, 2, 3, 0, 5,
		10, 3, 12, 18]
	n = len(a)
	q = [Query(0, 4),
		Query(4, 7),
		Query(7, 8)]
	m = len(q)
	RMQ(a, n, q, m)