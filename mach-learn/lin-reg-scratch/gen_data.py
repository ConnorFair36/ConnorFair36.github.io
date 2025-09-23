import pandas as pd
import numpy as np

def random_values(n: int, a: float, b: float, seed=42) -> tuple[np.ndarray, np.ndarray]:
	"""Returns n x values between [0, n] and y values between [a, b)."""
	np.random.seed(seed)
	return np.linspace(0, n, num=n*4), np.random.rand(n*4) * (b - a) + a

def random_line(n: int, m: float, b: float, mean: float, std: float, seed=42) -> tuple[np.ndarray, np.ndarray]:
	"""Returns values from 0 to n on the line mx+b but randomly offset from the line by a normal distribution."""
	np.random.seed(seed)
	noise = np.random.normal(loc=mean, scale=std, size=n*4)
	x: np.ndarray = np.linspace(0, n, num=n*4)
	y: np.ndarray =  (m * x) + b + noise
	return x, y

def quad_points(n: int, a: float, b: float, c: float) -> tuple[np.ndarray, np.ndarray]:
	"""Returns n values on the polynomial ax^2 + bx + c."""
	x: np.ndarray = np.linspace(0, n, num=n*4)
	y: np.ndarray = (a * x ** 2) + (b * x) + c
	return x, y

def anscombe_quartet() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
	"""Returns Anscombe's quartet. This dataset was found on wikipedia."""
	return (np.array([10.  ,  8.  , 13.  ,  9.  , 11.  , 14.  ,  6.  ,  4.  , 12.  ,
         7.  ,  5.  ], dtype=np.float32),
       np.array([ 8.04,  6.95,  7.58,  8.81,  8.33,  9.96,  7.24,  4.26, 10.84,
         4.82,  5.68], dtype=np.float32),
       np.array([10.  ,  8.  , 13.  ,  9.  , 11.  , 14.  ,  6.  ,  4.  , 12.  ,
         7.  ,  5.  ], dtype=np.float32),
       np.array([ 9.14,  8.14,  8.74,  8.77,  9.26,  8.1 ,  6.13,  3.1 ,  9.13,
         7.26,  4.74], dtype=np.float32),
       np.array([10.  ,  8.  , 13.  ,  9.  , 11.  , 14.  ,  6.  ,  4.  , 12.  ,
         7.  ,  5.  ], dtype=np.float32),
       np.array([ 7.46,  6.77, 12.74,  7.11,  7.81,  8.84,  6.08,  5.39,  8.15,
         6.42,  5.73], dtype=np.float32),
       np.array([ 8.  ,  8.  ,  8.  ,  8.  ,  8.  ,  8.  ,  8.  , 19.  ,  8.  ,
         8.  ,  8.  ], dtype=np.float32),
       np.array([ 6.58,  5.76,  7.71,  8.84,  8.47,  7.04,  5.25, 12.5 ,  5.56,
         7.91,  6.89], dtype=np.float32))

