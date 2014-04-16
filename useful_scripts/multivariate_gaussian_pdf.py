# Sebastian Raschka 04/2014

import numpy as np

def pdf_multivariate_gauss(x, mu, cov):
    '''
    Caculate the multivariate normal density (pdf)
    
    Keyword arguments:
        x = numpy array of a "d x 1" sample vector
        mu = numpy array of a "d x 1" mean vector
        cov = "numpy array of a d x d" covariance matrix
    '''
    assert(mu.shape[0] > mu.shape[1]), 'mu must be a row vector'
    assert(x.shape[0] > x.shape[1]), 'x must be a row vector'
    assert(cov.shape[0] == cov.shape[1]), 'covariance matrix must be square'
    assert(mu.shape[0] == cov.shape[0]), 'cov_mat and mu_vec must have the same dimensions'
    assert(mu.shape[0] == x.shape[0]), 'mu and x must have the same dimensions'
    part1 = 1 / ( ((2* np.pi)**(len(mu)/2)) * (np.linalg.det(cov)**(1/2)) )
    part2 = (-1/2) * ((x-mu).T.dot(np.linalg.inv(cov))).dot((x-mu))
    return float(part1 * np.exp(part2))

def test_gauss_pdf():
    from matplotlib.mlab import bivariate_normal

    x = np.array([[0],[0]])
    mu  = np.array([[0],[0]])
    cov = np.eye(2) 

    mlab_gauss = bivariate_normal(x,x)
    mlab_gauss = float(mlab_gauss[0]) # because mlab returns an np.array
    impl_gauss = pdf_multivariate_gauss(x, mu, cov)

    print('mlab_gauss:', mlab_gauss)
    print('impl_gauss:', impl_gauss)
    assert(mlab_gauss == impl_gauss), 'Implementations of the mult. Gaussian return different pdfs'


if __name__ == '__main__':
    test_gauss_pdf()
