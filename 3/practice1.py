import scipy.stats as stats

n = 10
p = 0.5
x= 7

#مقدار احتمال برنده شدن 
prob = stats.binom.pmf(x, n , p)
print(f'p(x=7) : {prob:.4f}')

#--------------------------------------