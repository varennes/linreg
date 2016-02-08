# example of the linreg function can do
import matplotlib.pyplot as plt
from scipy.stats import t
from math import sqrt

def linreg( X, Y):
    """
    Summary
        Linear regression of y = a*x + b
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


if __name__=='__main__':
    '''
    Test values from wikipedia (https://en.wikipedia.org/wiki/Simple_linear_regression)
    Compare results with those found in:
        https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_example
    '''
    X = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
    Y = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

    a, b, aerr, berr = linreg(X,Y)

    # make a line from y = b*x + a
    fitY = [ (a*x + b) for x in X]

    # print out results
    print 'a range: [{:.3}, {:.3}]'.format( a-aerr, a+aerr )
    print 'b range: [{:.3}, {:.3}]'.format( b-berr, b+berr )

    # plot of results
    alabel1 = '%.1f' %a
    alabel2 = '%.1f' %aerr
    afitLabel = 'slope = ' + alabel1 + r'$\pm$' + alabel2

    plt.plot( X, fitY, label=afitLabel)
    plt.plot( X, Y, 'o', label='data')

    plt.xlabel('x'); plt.ylabel('y')
    plt.legend(loc=4)
    plt.title('Simple Linear Regression')
    plt.show()
