
def ccy_classic_lstsqr(x, y):
    """ Computes the least-squares solution to a linear matrix equation. """
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)
    var_x = sum([(x_i - x_avg)**2 for x_i in x])
    cov_xy = sum([(x_i - x_avg)*(y_i - y_avg) for x_i,y_i in zip(x,y)])
    slope = cov_xy / var_x
    y_interc = y_avg - slope*x_avg
    return (slope, y_interc)