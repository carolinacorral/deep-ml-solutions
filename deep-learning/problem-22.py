""""
Problem: https://www.deep-ml.com/problem/Sigmoid%20Activation%20Function%20Understanding

""""

import math

def sigmoid(z: float) -> float:
	result = round((1 / (1 + math.exp(-z))),4)
	return result
