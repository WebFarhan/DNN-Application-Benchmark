# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
data = [89.7, 87.25, 89.67, 89.03, 87.83, 91.12, 89.18, 87.69, 86.84, 90.11, 88.36, 88.04, 91.63, 90.99, 89.05, 90.05, 91.18, 94.42, 93.19, 93.9, 93.84, 89.76, 87.04, 85.66, 87.62, 87.29, 89.03, 89.15, 86.85, 88.69]
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