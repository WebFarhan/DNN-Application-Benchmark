# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [109.79, 102.5, 111.41, 119.78, 102.32, 103.15, 109.1, 128.95, 109.06, 106.74, 115.68, 185.65, 108.33, 103.93, 101.68, 107.32, 113.77, 117.12, 103.79, 137.7, 171.41, 103.29, 109.22, 150.76, 107.9, 106.7, 106.28, 109.44, 106.5, 172.87]
stat, p = shapiro(data)
print('stat=%.3f, p=%.3f' % (stat, p))
f = open("NormalTestShapiro-Wilk.txt", "a")

if p > 0.05:
	print('Probably Gaussian')
	f.write('Probably Gaussian\n')
else:
	print('Probably not Gaussian')
	f.write('Probably not Gaussian\n')

f.write("Stat: {0}s and  p: {1}s\n".format(stat,p))

f.close()