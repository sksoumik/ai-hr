"""
https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

pearsons' coefficient of correlation formula can be found here:
https://businessjargons.com/karl-pearsons-coefficient-of-correlation.html

"""
import math


x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3] # Physics marks
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15] # History marks

x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)

x_std = 0
y_std = 0
corel= 0

for i in range(len(x)):
    x_std += (x[i] - x_mean)**2
    y_std += (y[i] - y_mean)**2
    corel += (x[i] - x_mean) * (y[i] - y_mean)

x_std = math.sqrt(x_std)
y_std = math.sqrt(y_std)
coef_corel = corel / (x_std * y_std)
print('%.3f'% coef_corel)


