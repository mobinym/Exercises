import scipy.stats as stats 


# احتمال یک لامپ معیوب بودن
p = 3 / 75

# محاسبه احتمال اینکه اولین لامپ معیوب در ششمین آزمایش پیدا شود
prob = stats.geom.pmf(6, p)
print(f'p(x=6) : {prob:.4f}')
