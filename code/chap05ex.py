import math
import random
import thinkstats2
import thinkplot

def pareto_variate(alpha):
    p = random.random()
    return 1 / math.exp(math.log(1-p) / alpha)

alpha = 7.8 
pareto1_random_numbers = [pareto_variate(alpha) for _ in range(1000)]
pareto2_random_numbers = [random.paretovariate(alpha) for _ in range(1000)]

cdf1 = thinkstats2.Cdf(pareto1_random_numbers)
cdf2 = thinkstats2.Cdf(pareto2_random_numbers)
thinkplot.PrePlot(2, cols=2)
thinkplot.Cdf(cdf1, color='blue')
thinkplot.Cdf(cdf2, color='gray')
thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Cdf(cdf1, complement=True, color='blue')
thinkplot.Cdf(cdf2, complement=True, color='gray')
thinkplot.Config(yscale='log', xscale='log')
thinkplot.Show()
