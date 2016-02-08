from scipy.stats import t
from math import sqrt

def linreg( X, Y):
    """
    Summary
        Simple Linear regression of y = a*x + b
    Usage
        real, real, real, real = linreg(list, list)
    Returns coefficients to the regression line "y=ax+b" from X and Y
    Returns error in extimated a and b values corresponding to 95% condience intervals
    """
    if len(X) != len(Y):  raise ValueError, 'unequal length'
    if len(X) < 2: raise ValueError, 'not sufficient data points'
    N = len(X)
    A = B = C = D = E = 0.0
    for x, y in map(None, X, Y):
        A = A + x
        B = B + y
        C = C + x*x
        D = D + y*y
        E = E + x*y

    # a = approximate slope
    # b = approximate y-intercept
    a = (N * E - A* B) / (N * C - A**2)
    b = (B / N) - (a * A / N)

    # standard error of a and b
    se2 = (1.0/(N*(N-2.0))) * (N * D - B**2 - (a**2) * (N * C - A**2))
    sa2 = (N * se2) / (N * C - A**2)
    sb2 = sa2 * C / N
    # tcrit = critical t value
    # using 0.975 gives 95% confidence intervals on a and b.
    tcrit = t.ppf(0.975,N-2)

    # +/- error in reported a and b values
    aerr = sqrt(sa2) * tcrit
    berr = sqrt(sb2) * tcrit

    return a, b, aerr, berr
