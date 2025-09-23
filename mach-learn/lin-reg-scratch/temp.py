import numpy as np

def pos_or_neg(x):
	pos = x > 0
	neg = x < 0
	x[pos] = 1
	x[neg] = -1
	return x