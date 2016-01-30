from scipy.stats import t
from math import sqrt

def linreg(X, Y):
    """
    Summary
        Linear regression of y = b*x + a
    Usage
        real, real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=bx+a" from X and Y
    Returns error in extimated a and b values corresponding to 95% condience intervals
    """
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    if len(X) < 2: raise ValueError, 'not sufficient data points'
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in map(None, X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y

    # b = approximate slope
    # a = approximate y-intercept
    b = (N * Sxy - Sx* Sy) / (N * Sxx - Sx**2)
    a = (Sy / N) - (b * Sx / N)

    # standard error of a and b
    se2 = (1.0/(N*(N-2.0))) * (N * Syy - Sy**2 - (b**2) * (N * Sxx - Sx**2))
    sb2 = (N * se2) / (N * Sxx - Sx**2)
    sa2 = sb2 * Sxx / N
    # tcrit = critical t value
    # using 0.975 gives 95% confidence intervals on a and b.
    tcrit = t.ppf(0.975,N-2)

    # +/- error in reported a and b values
    berr = sqrt(sb2) * tcrit
    aerr = sqrt(sa2) * tcrit

    return b, a, berr, aerr
