class SlowMatrix:

	## The constructor
	# @param matrix A 2d Python list containing data
	def __init__(self, matrix):
		self.matrix = matrix

	## Matrix multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __matmul__(self, mat2):
		result = [[0 for i in range(len(self.matrix))] for j in range(len(mat2.matrix[0]))]
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				for k in range(len(mat2.matrix)):
					result[i][j] += self.matrix[i][k] * mat2.matrix[k][j]
            	

		return SlowMatrix(result)

	## Element wise multiplication
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __mul__(self, mat2):
		result = [[0 for i in range(len(self.matrix))] for j in range(len(mat2.matrix[0]))]
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				result[i][j] = self.matrix[i][j] * mat2.matrix[i][j]
            	

		return SlowMatrix(result)

	## Element wise addition
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __add__(self, mat2):
		result = [[0 for i in range(len(self.matrix))] for j in range(len(mat2.matrix[0]))]
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				result[i][j] = self.matrix[i][j] + mat2.matrix[i][j]
            	

		return SlowMatrix(result)

	## Element wise subtraction
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __sub__(self, mat2):
		result = [[0 for i in range(len(self.matrix))] for j in range(len(mat2.matrix[0]))]
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				result[i][j] = self.matrix[i][j] - mat2.matrix[i][j]
            	

		return SlowMatrix(result)

	## Equality operator
	# @param self SlowMatrix1
	# @param mat2 SlowMatrix2
	def __eq__(self, mat2):
		result = True
		for i in range(len(self.matrix)):
			for j in range(len(mat2.matrix[0])):
				if (self.matrix[i][j] != mat2.matrix[i][j]):
					result = False
        

		return result

	## Calculate transpose
	def transpose(self):
		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				transpose[i][j] = self.matrix[j][i]
		
		return SlowMatrix(transpose)

	## Creates a SlowMatrix of 1s
	# @param shape A python pair (row, col)
	def ones(shape):
		for i in range(len(shape[0])):
			for j in range(len(shape[1])):
				ones[i][j] = 1
		return SlowMatrix(ones)
		

	## Creates a SlowMatrix of 0s
	# @param shape A python pair (row, col)
	def zeros(shape):
		for i in range(len(shape[0])):
			for j in range(len(shape[1])):
				zeros[i][j] = 0
		return SlowMatrix(zeros)

	## Returns i,jth element
	# @param key A python pair (i,j)
	def __getitem__(self, key):
		return self.matrix[key[0]][key[1]]

	## Sets i,jth element
	# @param key A python pair (i,j)
	# #param value Value to set
	def __setitem__(self, key, value):
		self.matrix[key[0]][key[1]] = value
		return SlowMatrix(self.matrix)

	## Converts SlowMatrix to a Python string
	def __str__(self):
		result = [[str(ele) for ele in sub] for sub in self.matrix]
		return result