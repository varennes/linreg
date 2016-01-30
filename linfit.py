from math import sqrt

def linfit(x,y,yerr):
    '''
        fit data points [x,y] with error in y-values, yerr
        to a line: f(x;a;b) = a*x + b
    '''
    if len(x) != len(y):  raise ValueError, 'unequal length'
    if len(y) != len(yerr):  raise ValueError, 'unequal length'
    if len(x) < 2: raise ValueError, 'not sufficient data points'
    n = len(x)
    A = B = C = D = E = F = 0.0

    for i in range(n):
        A += x[i] / (yerr[i]**2)
        B += 1.0 / (yerr[i]**2)
        C += y[i] / (yerr[i]**2)
        D += (x[i]**2) / (yerr[i]**2)
        E += x[i]*y[i] / (yerr[i]**2)
        F += (y[i]**2) / (yerr[i]**2)
    det = 1.0 / (B*D - A**2)

    a = det * (B*E - A*C)
    b = det * (C*D - A*E)

    aSigma = sqrt( det * B )
    bSigma = sqrt( det * D )

    chi2 = 0.0
    nu   = float(n - 2)

    for i in range(n):
        chi2 += ( (y[i] - a*x[i] - b) / yerr[i] )**2

    print 'reduced chi-squared = ' + str(chi2/nu)

    return a, b, aSigma, bSigma
