"""
Problem: https://www.deep-ml.com/problem/Calculate%20Mean%20by%20Row%20or%20Column

"""

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	n_rows = len(matrix)
	n_cols = len(matrix[0])
	means = []
	if mode == 'row':
		for i in range(n_rows):
			vals = []
			for j in range(n_cols):
				vals.append(matrix[i][j])
			if vals:
				means.append(np.mean(vals))
		
	if mode == 'column':
		for i in range(n_cols):
			vals = []
			for j in range(n_rows):
				vals.append(matrix[j][i])
			if vals:
				means.append(np.mean(vals))
		
	return means
