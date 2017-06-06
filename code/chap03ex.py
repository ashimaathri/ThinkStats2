import itertools

import nsfg
import thinkstats2
import thinkplot
import relay

def question1():
    resp = nsfg.ReadFemResp()
    numkdhh_pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
    biased_numkdhh_pmf = numkdhh_pmf.Copy(label='observed')
    for x in numkdhh_pmf:
        biased_numkdhh_pmf.Mult(x, x)
    biased_numkdhh_pmf.Normalize()
    print(numkdhh_pmf.Mean(), biased_numkdhh_pmf.Mean())
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([numkdhh_pmf, biased_numkdhh_pmf])
    thinkplot.Show(xlabel='number of children', ylabel='PMF')

def PmfMean(pmf):
    mean = 0

    for x, p in pmf.Items():
        mean += p * x

    return mean

def PmfVar(pmf):
    variance = 0
    mean = PmfMean(pmf)

    for x, p in pmf.Items():
        diff = (x - mean)
        variance += p * diff * diff 

    return variance

def question3():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    full_term = live[live.prglngth >= 37]
    preg_map = nsfg.MakePregMap(full_term)
    diffs = []
    for caseid, indices in preg_map.items():
        if len(indices) >= 2:
            diffs += [preg.prglngth[indices[0]] - preg.prglngth[other] for other in indices[1:]]
    pmf = thinkstats2.Pmf(diffs)
    print(pmf.Mean())
    thinkplot.Hist(pmf, align='center')
    thinkplot.Show(xlabel='Difference in weeks', ylabel='PMF')

def ObservedPmf(pmf, observer_speed):
    new_pmf = pmf.Copy(label='observed')
    for value, probability in pmf.Items():
        new_pmf[value] = abs(value - observer_speed) * probability
    new_pmf.Normalize()
    return new_pmf

results = relay.ReadResults()
speeds = relay.GetSpeeds(results)

speeds = relay.BinData(speeds, 3, 12, 100)

pmf = thinkstats2.Pmf(speeds, 'speeds')

observed_pmf = ObservedPmf(pmf, 7.5)

thinkplot.PrePlot(2)
thinkplot.pmfs([pmf, observed_pmf])
thinkplot.Show()
