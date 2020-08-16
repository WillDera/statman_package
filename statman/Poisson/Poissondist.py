import math
from scipy.stats import poisson
from random import seed
from ..Generaldistribution import statman

# import and setup seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize': (5, 5)})


class Poisson(statman):
    """
        Poisson distribution class for calculating and
        visualizing a Poisson distribution

        Attributes:
            mean (float) representing the mean value of the distribution,
            variance/var (float) representing the variance of the distribution,
            e (float) representing Euler's number,
            p (float) representing the probability of an occurance
            n (int) number of occurrences
    """

    def __init__(self, mu=0):

        statman.__init__(self)

        # constant
        self.e = 2.718282

    def get_mean_kurt_variance(self):
        """
            Function to get the mean of the data set.

            Args:
                None

            Returns:
                float: the mean value,
                float: the kurtosis value.
        """

        mean, variance, skew, kurt = poisson.stats(mu, moments='mvsk')

        self.mean = mean
        self.variance = variance
        self.kurt = kurt

        return mean, kurt, variance

    def calculate_probability(self, n):
        """
            Function to calculate the poisson probability of an occurance

            Args:
                e = Euler's number, 
                n = number of occurrences

            Returns:
                float: probability of the occurance of n

        """

        e = self.e
        mu = self.get_mean_kurt_variance()[0]

        n_factorial = math.factorial(n)
        e_negativeu = e ** -mu

        possion_prob = e_negativeu * mu ** n / n_factorial

        self.possion_prob = possion_prob
        self.n = n

        return possion_prob

    def plot_bar(self):
        """
            Function to output a histogram of the instance variable data using 
            seaborn library.

            Args:
                None

            Returns:
                None
        """

        mu = self.get_mean_kurt_variance()[0]
        s = seed(42)
        data_poisson = poisson.rvs(mu, size=seed)

        # sns distplot
        ax = sns.distplot(data_poisson, bins=30, kde=False, color='green',
                          hist_kws={"linewidth": 15, "alpha": 1})
        plot = ax.set(xlabel="Instances", ylabel="Probability")

        self.plot = plot

        return plot

    def pmf(self):
        """
            Probability mass function calculation for poisson distribution

            Args:
                mu (list): shape parameter for calculating the probability mass function
                k (float): kurtosis returned from the poisson.stats()

            Returns:
                float: probability mass function output
        """

        mu, k = self.get_mean_kurt_variance()

        k_factorial = math.factorial(k)
        m_exp = math.exp(-mu)

        return (m_exp * mu**k / k_factorial)

    def __repr__(self):
        """
            Function to output characteristics of the poisson instance

            Args:
                None

            Returns:
                string: characteristics of the Poisson
        """

        mean = self.mean
        var = self.kurt
        e = self.e
        p = self.possion_prob()
        n = self.n

        return ("mean: %s, variance: %s, e: %s, p: %s, n: %s" % (mean, var, e, p, n))
