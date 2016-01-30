# example of the linreg function can do
import matplotlib.pyplot as plt
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


if __name__=='__main__':
    '''
    Test values from wikipedia (https://en.wikipedia.org/wiki/Simple_linear_regression)
    Compare results with those found in:
        https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_example
    '''
    X = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
    Y = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

    b, a, berr, aerr = linreg(X,Y)

    # make a line from y = b*x + a
    fitY = [ (b*x + a) for x in X]

    # print out results
    print 'a range: [{:.3}, {:.3}]'.format( a-aerr, a+aerr )
    print 'b range: [{:.3}, {:.3}]'.format( b-berr, b+berr )

    # plot of results
    blabel1 = '%.1f' %b
    blabel2 = '%.1f' %berr
    bfitLabel = 'slope = ' + blabel1 + r'$\pm$' + blabel2

    plt.plot( X, fitY, label=bfitLabel)
    plt.plot( X, Y, 'o', label='data')

    plt.xlabel('x'); plt.ylabel('y')
    plt.legend(loc=4)
    plt.title('Simple Linear Regression')
    plt.show()
