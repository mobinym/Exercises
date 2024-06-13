import scipy.stats as stats 

n = 5
p = 2/3

# محاسبه احتمال اینکه بعد از 30 سال همه پنج نفر هنوز زنده باشند
prob_all_alive = stats.binom.pmf(5, n, p)
print(f'p(x=5) : {prob_all_alive:.4f}')

# محاسبه احتمال اینکه حداقل سه نفر هنوز زنده باشند
prob_at_least_three_alive = 1 - stats.binom.cdf(2, n, p)
print(f'p(x>3) : {prob_at_least_three_alive:.4f}')

# محاسبه احتمال اینکه دقیقاً دو نفر هنوز زنده باشند
prob_two_alive = stats.binom.pmf(2, n, p)
print(f'p(x=2) :{prob_two_alive:.4f}')

#-----------------------------------------------------------------------