import math
import random
import thinkstats2
import thinkplot
import numpy as np

def pareto_variate(alpha):
    p = random.random()
    return 1 / math.exp(math.log(1-p) / alpha)

#alpha = 7.8
#pareto1_random_numbers = [pareto_variate(alpha) for _ in range(1000)]
#pareto2_random_numbers = [random.paretovariate(alpha) for _ in range(1000)]
#
#cdf1 = thinkstats2.Cdf(pareto1_random_numbers)
#cdf2 = thinkstats2.Cdf(pareto2_random_numbers)
#thinkplot.PrePlot(2, cols=2)
#thinkplot.Cdf(cdf1, color='blue')
#thinkplot.Cdf(cdf2, color='gray')
#thinkplot.PrePlot(2)
#thinkplot.SubPlot(2)
#thinkplot.Cdf(cdf1, complement=True, color='blue')
#thinkplot.Cdf(cdf2, complement=True, color='gray')
#thinkplot.Config(yscale='log', xscale='log')
#thinkplot.Show()

k = 1
lam = 2
weibull_samples = [random.weibullvariate(2, 1) for _ in range(1000)]
weibull_cdf = thinkstats2.Cdf(weibull_samples)
xs, ps = weibull_cdf.Render()
xs = np.delete(xs, -1)
ps = np.delete(ps, -1)
ys = [-math.log(1-p) for p in ps]
thinkplot.plot(xs, ys)
thinkplot.Config(yscale='log', xscale='log')
thinkplot.Show()
