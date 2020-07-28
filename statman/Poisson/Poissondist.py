import math
from scipy.stats import poisson
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

    def __init__(self, mu=0.6):

        statman.__init__(self, mu)

        # constant
        self.e = 2.718282

    def calculate_mean(self):
        """
            Function to calculate the mean of the data set.

            Args:
                None

            Returns:
                Float: mean of the data set.
        """

        m, v, skew, kurt = poisson.stats(mu, moments='mvsk')

        mean = m

        return mean

    def calculate_probability(self, u, x):
        """
            Function to calculate the poisson probability of an occurance

            Args:
                e, 
                u = mean of the dataset
                x = expected occurance in a time frame

            Returns:
                float: probability of the occurance of x

        """

        x_factorial = math.factorial(self.x)
        e_negativeu = self.e ** -u

        possion_prob = e_negativeu * u ** x / x_factorial

        return possion_prob

    def pmf(self, mu, k):

        k_factorial = math.factorial(k)
        m_exp = math.exp(-mu)

        return (m_exp * mu**k / k_factorial)
