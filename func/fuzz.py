import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np
 
'''Функції приналежності'''
def triangular(x, a, b, c):
   f = fuzz.trimf(x, [a, b, c])
   plt.plot(x, f)
   plt.title("Трикутна функція приналежності")
   plt.show()
 
def trapecia(x, a, b, c, d):
   f = fuzz.trapmf(x, [a, b, c, d])
   plt.plot(x, f)
   plt.title("Трапицевидна функція приналежності")
   plt.show()
 
def qauss(x, mean, sigma):
   f = fuzz.gaussmf(x, mean, sigma)
   plt.plot(x, f)
   plt.title("Проста функція приналежності Гауса")
   plt.show()
  
def gauss2(x, mean1, sigma1, mean2, sigma2):
   f = fuzz.gauss2mf(x, mean1, sigma1, mean2, sigma2)
   plt.plot(x, f)
   plt.title("Двостороння функція приналежності Гауса")
   plt.show()
 
def bell(x, a, b, c):
   f = fuzz.gbellmf(x, a, b, c)
   plt.plot(x, f)
   plt.title("Функція приналежності узагальнений дзвін")
   plt.show()
 
def sigm(x, a, c):
   f = fuzz.sigmf(x, a, c)
   plt.plot(x, f)
   plt.title("Основна сигмоїдальна функція")
   plt.show()
 
def dsigm(x, a1, c1, a2, c2):
   f = fuzz.dsigmf(x, a1, c1, a2, c2)
   plt.plot(x, f)
   plt.title(f"Додаткова сигмоїдальна функція")
   plt.show()
 
def psigm(x, a1, c1, a2, c2):
   f = fuzz.psigmf(x, a1, c1, a2, c2)
   plt.plot(x, f)
   plt.title("Додаткова сигмоїдальна функція")
   plt.show()
 
def zf(x, a, b):
   f = fuzz.zmf(x, a, b)
   plt.plot(x, f)
   plt.title("Z-функції")
   plt.show()
 
def pif(x, a, b, c, d):
   f = fuzz.psigmf(x, a, b, c, d)
   plt.plot(x, f)
   plt.title("PI-функції")
   plt.show()
 
def sf(x, a, b):
   f = fuzz.smf(x, a, b)
   plt.plot(x, f)
   plt.title("S-функції")
   plt.show()
'''Максимінімальні мінімум та максимум'''
def min(x, f1, f2):
   z1, z2 = fuzz.fuzzy_and(x, f1, x, f2)
   z3, z4 = fuzz.fuzzy_or(x, f1, x, f2)
   plt.plot(z1, z2)
   plt.plot(z3, z4, linestyle='--')
   plt.title("Мінімум функції")
   plt.show()
 
def max(x, f1, f2):
   z1, z2 = fuzz.fuzzy_or(x, f1, x, f2)
   z3, z4 = fuzz.fuzzy_and(x, f1, x, f2)
   plt.plot(z1, z2)
   plt.plot(z3, z4, linestyle='--')
   plt.title("Максимум функції")
   plt.show()
'''Алгебраїчні мінімум та максимум з використання логічних операторів and та or'''
def min_and(x, f1, f2):
   f = f1 * f2
   plt.plot(x, f)
   plt.plot(x, f1, linestyle = '--')
   plt.plot(x, f2, linestyle = '--')
   plt.title("AND")
   plt.show()
 
def max_or(x, f1, f2):
   f = f1 + f2 - (f1 * f2)
   plt.plot(x, f)
   plt.plot(x, f1, linestyle = '--')
   plt.plot(x, f2, linestyle = '--')
   plt.title("OR")
   plt.show()
 
'''Доповнення'''
def f_not(x, f):
   func_not = fuzz.fuzzy_not(f)
   plt.plot(x, func_not)
   plt.plot(x, f, linestyle = '--')
   plt.title(f"(NOT)")
   plt.show()
 
 
x = np.arange(-12, 18, 0.1) #start, stop, step
triangular(x,  -6, 4, 8)
trapecia(x,-8, -2, 4, 6)
qauss(x,  4, 6)
gauss2(x,  -1, 6, 4, 8)
bell(x, 8, 6, 0)
sigm(x, 2, 2)
dsigm(x, -6, 4, 8, 2)
psigm(x, -6, 4, 8, 2)
zf(x, 2, 4)
pif(x, 1, 4, 6, 8)
sf(x, 0, 4)
 
f1 = fuzz.gaussmf(x, -1, 6)
f2 = fuzz.gaussmf(x, 3, 6)
max(x, f1, f2)
min(x, f1, f2)
max_or(x, f1, f2)
min_and(x, f1, f2)
f_not(x, f1)