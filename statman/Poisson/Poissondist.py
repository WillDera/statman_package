import math
from scipy.stats import poisson
from random import seed
from ..Generaldistribution import statman

# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize': (5, 5)})


class Poisson(statman):
    """
        Poisson distribution class for calculating and
        visualizing a Poisson distribution
    """

    def __init__(self, mu=0):

        statman.__init__(self)

        # constant
        self.e = 2.718282

    def calculate_mean(self):
        """
            Function to calculate the mean of the data set.

            Args:
                None

            Returns:
                mean (float): mean.
                kurt (float): kurtosis.
        """

        mean, variance, skew, kurt = poisson.stats(mu, moments='mvsk')

        return self.mean, self.kurt

    def calculate_probability(self, x):
        """
            Function to calculate the poisson probability of an occurance

            Args:
                e = the poisson constant, 
                x = expected occurance over a certain period

            Returns:
                float: probability of the occurance of x

        """

        e = self.e
        mu = self.calculate_mean()[0]

        x_factorial = math.factorial(x)
        e_negativeu = e ** -mu

        possion_prob = e_negativeu * mu ** x / x_factorial

        self.possion_prob = possion_prob

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

        mu = self.calculate_mean()[0]
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

        mu, k = self.calculate_mean()

        k_factorial = math.factorial(k)
        m_exp = math.exp(-mu)

        return (m_exp * mu**k / k_factorial)
