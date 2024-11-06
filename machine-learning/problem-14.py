"""
Problem: https://www.deep-ml.com/problem/Linear%20Regression%20Using%20Normal%20Equation

"""
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_1 = np.array(X)
	y_1 = np.array(y)
	theta = []
	thetas = np.linalg.inv(X_1.T.dot(X_1)).dot(X_1.T).dot(y_1)
	for th in thetas:
		theta.append(round(th,4))
	
	return theta
