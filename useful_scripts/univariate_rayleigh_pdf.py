import numpy as np

def comp_theta_mle(d):
    """
    Computes the Maximum Likelihood Estimate for a given 1D training
    dataset for a Rayleigh distribution.
    
    """
    theta = len(d) / sum([x**2  for x in d])
    return theta    

def likelihood_ray(x, theta):
    """
    Computes the class-conditional probability for an univariate
    Rayleigh distribution
    
    """
    return 2*theta*x*np.exp(-theta*(x**2))

if __name__ == "__main__":
    training_data = [10, 18, 19, 22, 24, 29, 33, 40, 68]
    theta = comp_theta_mle(training_data)

    # Plot Probability Density Function
    from matplotlib import pyplot as plt

    x_range = np.arange(0, 20, 0.1)
    y_range = [likelihood_ray(theta, x) for x in x_range]

    plt.figure(figsize=(10,8))
    plt.plot(x_range, y_range, lw=2)
    plt.title('Probability density function for the Rayleigh distribution')
    plt.ylabel('p(x)')
    plt.xlabel('random variable x')

    plt.show()
