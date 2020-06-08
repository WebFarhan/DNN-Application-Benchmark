# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [104.52, 104.24, 100.08, 102.43, 102.72, 103.59, 103.65, 103.7, 101.41, 103.13, 104.84, 102.92, 102.61, 102.62, 104.67, 102.34, 101.96, 100.63, 99.37, 104.64, 100.61, 101.78, 99.26, 100.35, 105.53, 105.65, 103.45, 102.75, 103.24, 104.67]
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