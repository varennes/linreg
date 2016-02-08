from math import sqrt

def linfit( X, Y, Yerr):
    '''
    Summary
        Linear regression of y = a*x + b
    Usage
        real, real, real, real = linreg(list, list, list)
    fit data points [X,Y] with error in Y-values, Yerr
    to a line: f(x;a;b) = a*x + b
    Returns coefficients to the regression line "y=ax+b" from X and Y, Yerr
    Returns error in extimated a and b values corresponding to 95% condience intervals
    '''
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    if len(Y) != len(Yerr):  raise ValueError, 'unequal length'
    if len(X) < 2: raise ValueError, 'not sufficient data points'
    n = len(X)
    A = B = C = D = E = F = 0.0

    for i in range(n):
        A += X[i] / (Yerr[i]**2)
        B += 1.0 / (Yerr[i]**2)
        C += Y[i] / (Yerr[i]**2)
        D += (X[i]**2) / (Yerr[i]**2)
        E += X[i]*Y[i] / (Yerr[i]**2)
        F += (Y[i]**2) / (Yerr[i]**2)
    det = 1.0 / (B*D - A**2)

    a = det * (B*E - A*C)
    b = det * (C*D - A*E)

    aSigma = sqrt( det * B )
    bSigma = sqrt( det * D )

    chi2 = 0.0
    nu   = float(n - 2)

    for i in range(n):
        chi2 += ( (Y[i] - a*X[i] - b) / Yerr[i] )**2

    print 'reduced chi-squared = ' + str(chi2/nu)

    return a, b, aSigma, bSigma
